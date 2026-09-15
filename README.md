# Machine Learning Zoomcamp — Coursework

My solutions for [ML Zoomcamp 2026](https://github.com/DataTalksClub/machine-learning-zoomcamp) by DataTalks.Club.

One module per week, starting 15 Sep 2026.

## Repository structure

```
.
├── 01-intro/              # Module 1: Introduction to Machine Learning
│   ├── data/              # Datasets — downloaded at runtime, not tracked
│   └── homework.ipynb     # Homework solutions
├── pyproject.toml         # Dependencies
└── .python-version        # Python 3.12
```

Each module lives in its own directory following the course numbering, with a
`homework.ipynb` holding that week's solutions. Datasets are downloaded from the
course repository by a cell inside each notebook and are not committed.

## Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync                 # create .venv and install dependencies
uv run jupyter lab      # launch Jupyter
```

Stack: NumPy, Pandas, scikit-learn, Matplotlib, Seaborn.

## Progress

| Module | Topic | Homework |
|---|---|---|
| 01 | Introduction to Machine Learning | ⬜ |
| 02 | Machine Learning for Regression | ⬜ |
| 03 | Machine Learning for Classification | ⬜ |
| 04 | Evaluation Metrics | ⬜ |
| 05 | Deploying Machine Learning Models | ⬜ |
| 06 | Decision Trees & Ensemble Learning | ⬜ |
| 07 | Midterm Project | ⬜ |
| 08 | Neural Networks & Deep Learning | ⬜ |
| 09 | Serverless Deep Learning | ⬜ |
| 10 | Kubernetes & TensorFlow Serving | ⬜ |
| — | Capstone Project | ⬜ |
