# Results (test, ROUGE F1 × 100)

Tuned on dev (objective: mean of R-1/R-2/R-L F1). Model: `bert-base-uncased`. Docs truncated to no sentence limit.


## cnn_dm

Budget = 3 sentences · 20 dev docs · 50 test docs

| System | Group | R-1 | R-2 | R-L | Tuned params |
|---|---|---:|---:|---:|---|
| random | bound | 27.13 | 8.26 | 24.01 | – |
| lead | baseline | 38.83 | 16.05 | 34.86 | – |
| oracle | bound | 57.00 | 35.77 | 53.23 | – |
| degree_tfidf | baseline | 34.12 | 14.57 | 31.50 | beta=0.0 |
| textrank | baseline | 34.51 | 14.31 | 31.36 | – |
| lexpagerank | baseline | 33.43 | 12.90 | 30.51 | – |
| pacsum_tfidf | baseline | 39.44 | 18.31 | 36.14 | beta=0.0, lambda1=-1.0 |
| full_pipeline | ours | 30.88 | 9.69 | 27.30 | beta=0.6, gamma=2.0, memory=0.5 |
| abl_position | ablation | 38.82 | 16.79 | 35.21 | beta=0.0, forward_weight=-2.0, gamma=2.0, memory=0.9 |
| abl_positive_pagerank | ablation | 30.55 | 9.66 | 27.09 | beta=0.6 |
| abl_degree | ablation | 28.67 | 8.22 | 25.75 | beta=0.6 |

Graph diagnostics on test (share of kept cross-sentence pairs that NSP directed / rejected both ways; share of docs where every sentence tied, which reduces to Lead):

| System | directed | rejected | all-tied docs |
|---|---:|---:|---:|
| full_pipeline | 0.988 | 0.012 | 0.02 |
| abl_position | 0.0 | 0.0 | 0.0 |
| abl_positive_pagerank | 0.988 | 0.012 | 0.02 |
| abl_degree | 0.988 | 0.012 | 0.02 |

Oracle sentence positions by document decile (first → last): [0.264, 0.16, 0.152, 0.096, 0.112, 0.072, 0.032, 0.024, 0.056, 0.032]; mean relative position 0.309.
