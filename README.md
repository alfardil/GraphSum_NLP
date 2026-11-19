# Graph-based extractive summarization: frozen-BERT direction + PageTrust

| File | What it does |
|---|---|
| `bert_graph.py` | vertices (sentences or clauses), frozen BERT vectors, PacSum β threshold, NSP direction, negative edges, λ |
| `splitting.py` | sentence / clause / reference splitting, matched to the team's `ranking/` (NLTK punkt, arXiv/PubMed pre-split, rule-based clauses) |
| `rankers.py` | PageTrust (de Kerchove & Van Dooren 2008, Alg. 4.1), PageRank, degree; numerically identical to `ranking/pagetrust.py` |
| `baselines.py` | stemmed preprocessing, Lead, Random, Oracle, Degree (TF-IDF), TextRank, LexPageRank, PacSum (TF-IDF) |
| `data.py` | loaders for CNN/DM, arXiv, PubMed, tldr-17, WikiHow, BillSum; 80/10/10 pooled splits |
| `pipeline.py` | every system behind one interface + `Summarizer` for single documents |
| `evaluate.py` | dev tuning → test ROUGE-1/2/L F1, ablations, error-analysis logs |

```bash
pip install -r requirements.txt && python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt_tab')"
python evaluate.py --datasets cnn_dm --limit-dev 200 --limit-test 1000   # or ./run_eval.sh for everything
```

Results go to `results/results.md` (tables), `results.json` (plus every dev grid point),
`per_doc.jsonl` (per-document selections and ROUGE, for targeted inspection) and Oracle
position deciles (for the position analysis).

## Compatibility with the team repo
This is the `graph/` folder of [Motabagani/graph-summarization](https://github.com/Motabagani/graph-summarization).
- **Interface.** `build_graph(...).W` is the team's `W`: `W[i, j] > 0` is an edge i → j, `< 0` means NSP rejected both orders, and the diagonal is ignored. Pass it to `ranking/pagetrust.py: pagetrust(W, alpha, gamma, memory)`.
- **Using the team Preprocessor's units:** `vertices_from_units(doc.units, doc.unit_sentence)` builds vertices from a `ranking/preprocess.py` `Document`.
- **Same defaults as `ranking/`:** NLTK punkt sentences; arXiv/PubMed pre-split at `" ."` tokens; references split like `ranking/run.py: ref_lines`; rule-based clauses (`ranking/preprocess.py: split_clauses`); max over a sentence's clause scores (`ranking/selector.py`); the same budgets and tie-breaking; `cnndm` is accepted as an alias for `cnn_dm`. The original graphsum setup is still available: `--splitter spacy --clause-splitter spacy --aggregate mean`.
- **Check:** `tests/test_team_compat.py` compares rankers, budgets and selection, splitting and aggregation against the team code. It finds `ranking/` at `../ranking`, or at `$TEAM_RANKING`.
- `results/small/` and `results/analysis/` predate these changes: they used spaCy splitting and the old PageTrust stopping rule, which differed from the team's at γ = ∞. Re-run before comparing them with team numbers.

## Conventions and choices
- `W[i, j]` is an edge i → j (i endorses j). If NSP finds "A then B" more plausible, B builds on A, so the edge is B → A.
- NSP rejects both orders (isNext log-odds < 0 both ways) → negative edge both ways. Confidence = tanh(|Δ log-odds| / 2), because NSP probabilities saturate near 1 for in-document pairs.
- Fixed: α = 0.85, ε = 1e-6, at most 100 iterations. Tuned on dev: β ∈ {0, .3, .6}, γ ∈ {0, 1, 2, ∞}, M ∈ {0, .5, .9, 1} (the proposal's {0, 1} plus the team's {0, .5, .9}); λ ∈ {0, .5, 1} for clauses; PacSum λ1 ∈ {−2, −1, −.5, 0} with λ2 = 1.
- Summary length: the team's fixed per-dataset budgets, shared with the baselines in the team repo (`TEAM_BUDGETS` in `evaluate.py`: CNN/DM 3 sentences, tldr 1 sentence, PubMed 203 words, arXiv 220, BillSum 184, WikiHow 55). Word budgets add sentences best-first until the budget is reached; `--overflow` sets the rule for the sentence that crosses it (default `include`). `--length median` uses the median number of dev reference sentences instead (always the case for `--synthetic`), and `--n K` forces K sentences.
- ROUGE uses Google's `rouge-score` (stemmed, ROUGE-Lsum), so numbers are close to, but not identical with, the Perl ROUGE-1.5.5 figures quoted from PacSum/HipoRank.
- Read the graph diagnostics under each table. A high "all-tied docs" share means NSP left too few positive edges and the system fell back to Lead through tie-breaking.

## Cost
NSP needs two BERT passes per sentence pair that survives the threshold. β = 0 keeps every pair, so a 200-sentence arXiv paper costs ~40k passes. That's fine on a GPU for CNN/DM and tldr, but for long documents use `--max-sentences` and `--betas 0.3 0.6` (as `run_eval.sh` does). It's impractical on CPU beyond small samples.

## Offline check (no downloads)
```bash
python tests/make_tiny_bert.py /tmp/tinybert
python evaluate.py --synthetic --model /tmp/tinybert --limit-dev 20 --limit-test 30 --clauses
```
