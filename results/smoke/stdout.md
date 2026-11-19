# Results (test, ROUGE F1 × 100)

Tuned on dev (objective: mean of R-1/R-2/R-L F1). Model: `bert-base-uncased`. Docs truncated to no sentence limit.


## cnn_dm

N = 4 sentences · 20 dev docs · 50 test docs

| System | Group | R-1 | R-2 | R-L | Tuned params |
|---|---|---:|---:|---:|---|
| lead | baseline | 37.60 | 15.98 | 33.95 | – |
| oracle | bound | 57.72 | 35.99 | 53.95 | – |
| full_pipeline | ours | 29.82 | 9.59 | 26.66 | beta=0.0, gamma=∞, memory=1.0 |
| abl_position | ablation | 37.60 | 15.98 | 33.95 | beta=0.0, forward_weight=-2.0, gamma=∞, memory=0.0 |

Graph diagnostics on test (share of kept cross-sentence pairs that NSP directed / rejected both ways; share of docs where every sentence tied, which reduces to Lead):

| System | directed | rejected | all-tied docs |
|---|---:|---:|---:|
| full_pipeline | 0.825 | 0.175 | 0.0 |
| abl_position | 0.0 | 0.0 | 0.0 |

Oracle sentence positions by document decile (first → last): [0.271, 0.164, 0.15, 0.107, 0.1, 0.071, 0.029, 0.021, 0.05, 0.036]; mean relative position 0.301.
