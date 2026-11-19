# Results (test, ROUGE F1 × 100)

Tuned on dev (objective: mean of R-1/R-2/R-L F1). Model: `bert-base-uncased`. Docs truncated to no sentence limit.


## tldr

Budget = 1 sentences · 20 dev docs · 50 test docs

| System | Group | R-1 | R-2 | R-L | Tuned params |
|---|---|---:|---:|---:|---|
| random | bound | 13.11 | 2.11 | 10.95 | – |
| lead | baseline | 12.78 | 2.35 | 11.11 | – |
| oracle | bound | 22.67 | 7.16 | 19.38 | – |
| degree_tfidf | baseline | 13.33 | 2.55 | 11.11 | beta=0.6 |
| textrank | baseline | 14.57 | 1.97 | 11.38 | – |
| lexpagerank | baseline | 14.34 | 2.21 | 11.56 | – |
| pacsum_tfidf | baseline | 15.09 | 2.78 | 12.48 | beta=0.0, lambda1=0.0 |
| full_pipeline | ours | 10.69 | 2.52 | 9.21 | beta=0.3, gamma=∞, memory=0.5 |
| abl_position | ablation | 14.03 | 3.05 | 12.15 | beta=0.6, forward_weight=-2.0, gamma=1.0, memory=0.5 |
| abl_positive_pagerank | ablation | 9.44 | 1.96 | 8.21 | beta=0.3 |
| abl_degree | ablation | 10.75 | 1.32 | 8.47 | beta=0.6 |

Graph diagnostics on test (share of kept cross-sentence pairs that NSP directed / rejected both ways; share of docs where every sentence tied, which reduces to Lead):

| System | directed | rejected | all-tied docs |
|---|---:|---:|---:|
| full_pipeline | 0.819 | 0.181 | 0.0 |
| abl_position | 0.0 | 0.0 | 0.0 |
| abl_positive_pagerank | 0.819 | 0.181 | 0.0 |
| abl_degree | 0.958 | 0.042 | 0.0 |

Oracle sentence positions by document decile (first → last): [0.36, 0.02, 0.12, 0.08, 0.08, 0.04, 0.06, 0.08, 0.04, 0.12]; mean relative position 0.373.
