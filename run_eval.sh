#!/usr/bin/env bash
# One-shot evaluation on a GPU machine (e.g. NYU Greene: run inside an sbatch job with --gres=gpu:1).
set -euo pipefail
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt_tab')"
python tests/test_rankers.py && python tests/logic.py && python tests/test_budget.py && python tests/test_team_compat.py

# Short documents: full β grid.
python evaluate.py --datasets cnn_dm tldr --limit-dev 200 --limit-test 1000 --out results/short

# Long documents: cap length and skip β=0 (which runs NSP on every sentence pair).
python evaluate.py --datasets arxiv pubmed billsum --limit-dev 100 --limit-test 500 \
    --max-sentences 150 --betas 0.3 0.6 --out results/long

# WikiHow needs the CSV from https://github.com/mahnazkoupaee/WikiHow-Dataset
if [ -f wikihowAll.csv ]; then
  python evaluate.py --datasets wikihow --wikihow-csv wikihowAll.csv --limit-dev 200 --limit-test 1000 --out results/wikihow
fi
