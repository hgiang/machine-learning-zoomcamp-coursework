"""Q3 — load pipeline.bin with pickle and score one lead.

Run inside the locked release environment:

    cd release && uv run python ../q3_predict.py
"""

import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "release" / "pipeline.bin"

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

with MODEL_PATH.open("rb") as f_in:
    pipeline = pickle.load(f_in)

probability = pipeline.predict_proba([lead])[0, 1]
print(f"conversion probability = {probability:.6f} -> {probability:.3f}")
