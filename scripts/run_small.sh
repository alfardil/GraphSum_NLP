#!/usr/bin/env bash
# Small preview runs on a laptop GPU (Apple MPS): one evaluate.py run per dataset, each under ~1 h.
# NOT the reportable runs (those are run_eval.sh on the HPC). Results: results/small/<dataset>/.
set -uo pipefail
cd "$(dirname "$0")/.."
DEV=${DEV:-mps}
python tests/test_rankers.py && python tests/logic.py && python tests/test_budget.py && python tests/test_team_compat.py || exit 1

# Short documents: full β grid.
for ds in cnn_dm tldr; do
  scripts/run_logged.sh results/small/$ds python evaluate.py --datasets $ds \
      --limit-dev 20 --limit-test 50 --device $DEV --batch-size 32 --seed 0 --out results/small/$ds
  echo "$ds exit=$?"
done

# Long documents: first 60 sentences, β ∈ {0.3, 0.6} (as run_eval.sh), fewer docs.
for ds in billsum pubmed arxiv; do
  scripts/run_logged.sh results/small/$ds python evaluate.py --datasets $ds \
      --limit-dev 15 --limit-test 40 --max-sentences 60 --betas 0.3 0.6 \
      --device $DEV --batch-size 32 --seed 0 --out results/small/$ds
  echo "$ds exit=$?"
done

# WikiHow only if the CSV is present (the GitHub source is gone; get it from a teammate).
if [ -f wikihowAll.csv ]; then
  scripts/run_logged.sh results/small/wikihow python evaluate.py --datasets wikihow --wikihow-csv wikihowAll.csv \
      --limit-dev 20 --limit-test 50 --device $DEV --batch-size 32 --seed 0 --out results/small/wikihow
  echo "wikihow exit=$?"
fi
python scripts/merge_tables.py results/small/* --out results/small/paper_tables
echo "all done"
