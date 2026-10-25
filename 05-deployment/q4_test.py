"""Q4/Q6 client — send the second lead to a running API.

    python q4_test.py                              # default http://localhost:9696
    python q4_test.py http://localhost:9696
"""

import json
import sys
from urllib.request import Request, urlopen

base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:9696"

lead = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74,
}

with urlopen(f"{base_url}/health") as response:
    print("health:", json.load(response))

request = Request(
    f"{base_url}/predict",
    data=json.dumps(lead).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urlopen(request) as response:
    result = json.load(response)

assert 0 <= result["conversion_probability"] <= 1
assert isinstance(result["conversion"], bool)
print("predict:", result)
print(f"-> {result['conversion_probability']:.3f}")
