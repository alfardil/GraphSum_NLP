"""Measure where pipeline time goes (checkpoint 3): NSP pairs/sec on the device, plus the
cost of embedding, build_graph and pagetrust per document.

    python scripts/nsp_throughput.py --dataset cnn_dm --docs 5 --device mps

Uses real test documents so pair lengths (and therefore padding) are realistic. Also
reports, for each β in the grid, the share of cross-sentence pairs kept by the threshold,
which is what sets the number of NSP calls (NSP runs on the union over the grid, i.e. the
smallest β).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import spacy  # noqa: E402
import torch  # noqa: E402

from bert_graph import DocumentScores, FrozenBert, GraphConfig, build_graph, make_vertices  # noqa: E402
from data import load_split  # noqa: E402
from rankers import pagetrust  # noqa: E402


def sync(dev):
    if dev == "cuda":
        torch.cuda.synchronize()
    elif dev == "mps":
        torch.mps.synchronize()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="cnn_dm")
    ap.add_argument("--docs", type=int, default=5)
    ap.add_argument("--max-sentences", type=int, default=None)
    ap.add_argument("--model", default="bert-base-uncased")
    ap.add_argument("--device", default=None)
    ap.add_argument("--batch-size", type=int, default=64)
    ap.add_argument("--nsp-max-length", type=int, default=256)
    ap.add_argument("--max-pairs", type=int, default=4000, help="cap NSP pairs timed per doc")
    ap.add_argument("--wikihow-csv", default=None)
    ap.add_argument("--graph-beta", type=float, default=0.0,
                    help="β for timing build_graph (NSP is run on the pairs it keeps)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    nlp = spacy.load("en_core_web_sm")
    enc = FrozenBert(args.model, device=args.device, batch_size=args.batch_size, max_length=args.nsp_max_length)
    exs = load_split(args.dataset, "test", args.docs, nlp, 0, args.wikihow_csv)
    # warm-up (kernel compilation / allocator)
    enc.nsp_logodds(["warm up sentence ."] * args.batch_size, ["another one ."] * args.batch_size)
    sync(enc.device)

    tot = {"pairs": 0, "nsp_s": 0.0, "embed_s": 0.0, "graph_s": 0.0, "pagetrust_s": 0.0, "sents": []}
    keep = {b: [] for b in (0.0, 0.3, 0.6)}
    for ex in exs:
        spans = [s for s in nlp(ex.text).sents if s.text.strip()][: args.max_sentences]
        verts = make_vertices(spans)
        n = len(verts)
        tot["sents"].append(n)
        t = time.perf_counter(); S = DocumentScores(verts, enc); sync(enc.device); tot["embed_s"] += time.perf_counter() - t
        iu = np.triu_indices(n, 1)
        off = S.sim[iu]
        for b in keep:
            keep[b].append(float((off >= off.min() + b * (off.max() - off.min())).mean()))
        pairs = [(int(i), int(j)) for i, j in zip(*iu)][: args.max_pairs]
        t = time.perf_counter(); S.nsp(pairs); sync(enc.device); dt = time.perf_counter() - t
        tot["nsp_s"] += dt; tot["pairs"] += 2 * len(pairs)       # 2 ordered passes per pair
        cfg = GraphConfig(beta=args.graph_beta)
        # time build_graph on a fully cached NSP table, so this is pure Python/numpy cost
        th = off.min() + cfg.beta * (off.max() - off.min())
        S.nsp([(int(i), int(j)) for i, j in zip(*iu) if S.sim[i, j] >= th])
        t = time.perf_counter(); G = build_graph(S, cfg); tot["graph_s"] += time.perf_counter() - t
        t = time.perf_counter(); pagetrust(G.W, gamma=1.0, memory=1.0); tot["pagetrust_s"] += time.perf_counter() - t
        print(f"{ex.id}: n={n}, {2 * len(pairs)} NSP passes in {dt:.2f}s", file=sys.stderr)

    nd = len(exs)
    rep = {
        "dataset": args.dataset, "device": enc.device, "batch_size": args.batch_size,
        "nsp_max_length": args.nsp_max_length, "docs": nd,
        "mean_sentences": round(float(np.mean(tot["sents"])), 1),
        "nsp_passes_per_sec": round(tot["pairs"] / tot["nsp_s"], 1),
        "graph_beta": args.graph_beta,
        "embed_s_per_doc": round(tot["embed_s"] / nd, 3),
        "build_graph_s_per_doc": round(tot["graph_s"] / nd, 4),
        "pagetrust_s_per_call": round(tot["pagetrust_s"] / nd, 4),
        "kept_pair_share_by_beta": {str(b): round(float(np.mean(v)), 3) for b, v in keep.items()},
    }
    print(json.dumps(rep, indent=1))
    if args.out:
        Path(args.out).write_text(json.dumps(rep, indent=1))


if __name__ == "__main__":
    main()
