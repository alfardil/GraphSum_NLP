"""Smoke-test diagnostics for the NSP edges (checkpoint 2).

    python scripts/nsp_diagnostics.py --run results/smoke --docs 3 --device mps

1. For the first --docs test documents, runs NSP on every cross-sentence pair kept at the tuned
   β of full_pipeline (read from results.json) and prints the distribution of
   |Δ log-odds| = |logodds(i then j) - logodds(j then i)| for directed pairs, the resulting
   confidence tanh(|Δ|/2), and the share of pairs rejected both ways.
2. From per_doc.jsonl, compares full_pipeline's selections with Lead's on every test doc.
Writes results to <run>/nsp_diagnostics.json as well as stdout.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import spacy  # noqa: E402

from bert_graph import DocumentScores, FrozenBert, make_vertices  # noqa: E402
from data import load_split  # noqa: E402


def quantiles(x):
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return {}
    qs = [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]
    return {f"q{int(q * 100)}": round(float(np.quantile(x, q)), 3) for q in qs} | {"mean": round(float(x.mean()), 3)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="results/smoke")
    ap.add_argument("--dataset", default="cnn_dm")
    ap.add_argument("--docs", type=int, default=3)
    ap.add_argument("--limit-test", type=int, default=50, help="must match the run, so sampling matches")
    ap.add_argument("--model", default="bert-base-uncased")
    ap.add_argument("--device", default=None)
    ap.add_argument("--nsp-max-length", type=int, default=256)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    run = Path(args.run)
    res = json.loads((run / "results.json").read_text())[args.dataset]
    beta = res["systems"]["full_pipeline"]["params"]["beta"]

    out = {"beta": beta, "docs": []}
    nlp = spacy.load("en_core_web_sm")
    enc = FrozenBert(args.model, device=args.device, max_length=args.nsp_max_length)
    exs = load_split(args.dataset, "test", args.limit_test, nlp, args.seed)[: args.docs]
    print(f"tuned beta = {beta}")
    for ex in exs:
        verts = make_vertices(ex.text, nlp)
        S = DocumentScores(verts, enc)
        n = S.n
        iu = np.triu_indices(n, 1)
        off = S.sim[iu]
        thresh = off.min() + beta * (off.max() - off.min())
        pairs = [(int(i), int(j)) for i, j in zip(*iu) if S.sim[i, j] >= thresh]
        lo = S.nsp(pairs)
        d = np.array([a - b for a, b in lo.values()])
        both_neg = np.array([a < 0 and b < 0 for a, b in lo.values()])
        both_pos = np.array([a >= 0 and b >= 0 for a, b in lo.values()])
        raw = np.array([v for ab in lo.values() for v in ab])
        directed_abs = np.abs(d[~both_neg])
        rec = {
            "doc": ex.id, "n_sentences": n, "kept_pairs": len(pairs),
            "rejected_share": round(float(both_neg.mean()), 3),
            "both_orders_accepted_share": round(float(both_pos.mean()), 3),
            "raw_logodds": quantiles(raw),
            "abs_delta_directed": quantiles(directed_abs),
            "confidence_directed": quantiles(np.tanh(directed_abs / 2)),
            "share_conf_below_0.1": round(float((np.tanh(directed_abs / 2) < 0.1).mean()), 3) if directed_abs.size else None,
            # adjacent pairs in the true order: does NSP get the original order right?
            "adjacent_true_order_preferred": round(float(np.mean(
                [lo[(i, i + 1)][0] > lo[(i, i + 1)][1] for i in range(n - 1) if (i, i + 1) in lo]
            )), 3) if any((i, i + 1) in lo for i in range(n - 1)) else None,
        }
        out["docs"].append(rec)
        print(json.dumps(rec, indent=1))

    # selections vs Lead
    rows = [json.loads(l) for l in open(run / "per_doc.jsonl")]
    by = {}
    for r in rows:
        if r["dataset"] == args.dataset:
            by.setdefault(r["system"], {})[r["doc"]] = r
    lead, ours = by["lead"], by["full_pipeline"]
    same = [d for d in ours if ours[d]["selected"] == lead[d]["selected"]]
    overlap = [len(set(ours[d]["selected"]) & set(lead[d]["selected"])) / max(len(lead[d]["selected"]), 1) for d in ours]
    out["vs_lead"] = {"docs": len(ours), "identical_to_lead": len(same),
                      "identical_share": round(len(same) / max(len(ours), 1), 3),
                      "mean_overlap_with_lead": round(float(np.mean(overlap)), 3),
                      "mean_first_pick_position": round(float(np.mean([min(ours[d]["selected"]) for d in ours])), 2)}
    if "abl_position" in by:
        pos = by["abl_position"]
        out["vs_lead"]["abl_position_identical_to_lead"] = sum(pos[d]["selected"] == lead[d]["selected"] for d in pos)
    print(json.dumps(out["vs_lead"], indent=1))
    (run / "nsp_diagnostics.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
