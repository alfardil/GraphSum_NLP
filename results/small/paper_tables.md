# Paper tables

### Table 1. Main results (test ROUGE F1 × 100)

| System | CNN/DM R-1 | R-2 | R-L | tldr-17 R-1 | R-2 | R-L |
|---|---:|---:|---:|---:|---:|---:|
| Oracle | 57.00 | 35.77 | 53.23 | 22.67 | 7.16 | 19.38 |
| Random | 27.13 | 8.26 | 24.01 | 13.11 | 2.11 | 10.95 |
| Lead | 38.83 | 16.05 | 34.86 | 12.78 | 2.35 | 11.11 |
| Degree (TF-IDF) | 34.12 | 14.57 | 31.50 | 13.33 | 2.55 | 11.11 |
| TextRank | 34.51 | 14.31 | 31.36 | 14.57 | 1.97 | 11.38 |
| LexPageRank | 33.43 | 12.90 | 30.51 | 14.34 | 2.21 | 11.56 |
| PacSum (TF-IDF) | **39.44** | **18.31** | **36.14** | **15.09** | **2.78** | **12.48** |
| Ours: BERT-NSP + PageTrust | 30.88 | 9.69 | 27.30 | 10.69 | 2.52 | 9.21 |

### Table 2. Ablations (test ROUGE F1 × 100)

| System | CNN/DM R-1 | R-2 | R-L | tldr-17 R-1 | R-2 | R-L |
|---|---:|---:|---:|---:|---:|---:|
| Ours: BERT-NSP + PageTrust | 30.88 | 9.69 | 27.30 | 10.69 | 2.52 | 9.21 |
| − NSP direction, + position heuristic | **38.82** | **16.79** | **35.21** | **14.03** | **3.05** | **12.15** |
| − negative edges (PageRank) | 30.55 | 9.66 | 27.09 | 9.44 | 1.96 | 8.21 |
| − PageTrust (in-degree) | 28.67 | 8.22 | 25.75 | 10.75 | 1.32 | 8.47 |

Notes:
- **CNN/DM**: N = 3, 20 dev / 50 test docs (`results/small/cnn_dm`). Ours tuned: beta=0.6, gamma=2.0, memory=0.5. NSP directed 0.988, rejected 0.012, all-tied docs 0.02.
- **tldr-17**: N = 1, 20 dev / 50 test docs (`results/small/tldr`). Ours tuned: beta=0.3, gamma=inf, memory=0.5. NSP directed 0.819, rejected 0.181, all-tied docs 0.0.
