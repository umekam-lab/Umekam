"""Weighted comparison of the five shortlisted candidates.

Scores are 1-5 (5 = best; for capital exposure 5 = least capital at risk).
Run: python3 scoring.py
"""

CRITERIA = ["demand", "reach", "fit", "margin", "diff", "feasibility", "capital", "growth"]

BASE_WEIGHTS = {"demand": .20, "reach": .15, "fit": .15, "margin": .10,
                "diff": .10, "feasibility": .10, "capital": .10, "growth": .10}

# Central scores, plus a (low, high) range on the criteria where evidence is thinnest.
CANDIDATES = {
    "A Robust environments (furniture/fixtures)": {
        "score": {"demand": 3, "reach": 4, "fit": 5, "margin": 3, "diff": 3,
                  "feasibility": 4, "capital": 4, "growth": 3},
        "uncertain": {"demand": (2, 4), "reach": (3, 4), "margin": (2, 4)},
        "confidence": "low",
    },
    "B Staff safety alarms + incident follow-up": {
        "score": {"demand": 4, "reach": 4, "fit": 5, "margin": 3, "diff": 2,
                  "feasibility": 2, "capital": 3, "growth": 3},
        "uncertain": {"diff": (1, 3), "feasibility": (2, 3), "margin": (2, 4)},
        "confidence": "medium",
    },
    "C Estate clearance & senior-move coordination": {
        "score": {"demand": 4, "reach": 3, "fit": 3, "margin": 3, "diff": 2,
                  "feasibility": 2, "capital": 5, "growth": 2},
        "uncertain": {"reach": (2, 4), "margin": (2, 3)},
        "confidence": "medium",
    },
    "D Board maintenance 'living plan'": {
        "score": {"demand": 3, "reach": 2, "fit": 3, "margin": 3, "diff": 1.5,
                  "feasibility": 3, "capital": 4, "growth": 3},
        "uncertain": {"demand": (2, 3), "reach": (2, 3)},
        "confidence": "medium",
    },
    "E Holiday-home monitoring + partner inspection": {
        "score": {"demand": 3, "reach": 2, "fit": 2, "margin": 2.5, "diff": 3,
                  "feasibility": 3, "capital": 3, "growth": 3},
        "uncertain": {"demand": (2, 4), "margin": (2, 3)},
        "confidence": "medium-low",
    },
}

SCENARIOS = {
    "Base weights": BASE_WEIGHTS,
    "Demand-heavy (demand 30%, fit 10%, feasibility 5%)":
        {**BASE_WEIGHTS, "demand": .30, "fit": .10, "feasibility": .05},
    "Growth-heavy (growth 25%, capital 5%, feasibility 5%, fit 10%)":
        {**BASE_WEIGHTS, "growth": .25, "capital": .05, "feasibility": .05, "fit": .10},
    "Capital-blind (capital 0%, demand 25%, diff 15%)":
        {**BASE_WEIGHTS, "capital": .0, "demand": .25, "diff": .15},
    "Founder-fit ignored (fit 0%, demand 25%, reach 20%, margin 15%)":
        {**BASE_WEIGHTS, "fit": .0, "demand": .25, "reach": .20, "margin": .15},
    "Equal weights": {c: 1 / 8 for c in CRITERIA},
}


def total(scores, weights):
    assert abs(sum(weights.values()) - 1) < 1e-9, weights
    return sum(scores[c] * weights[c] for c in CRITERIA)


def ranged(cand, weights, pick):
    s = dict(cand["score"])
    for c, (lo, hi) in cand["uncertain"].items():
        s[c] = lo if pick == "low" else hi
    return total(s, weights)


if __name__ == "__main__":
    print("## Base-weight scores with uncertainty ranges\n")
    print("| Candidate | " + " | ".join(CRITERIA) + " | Weighted | Low | High | Confidence |")
    print("|---|" + "---|" * (len(CRITERIA) + 4))
    for name, cand in CANDIDATES.items():
        s = cand["score"]
        print(f"| {name} | " + " | ".join(f"{s[c]:g}" for c in CRITERIA)
              + f" | {total(s, BASE_WEIGHTS):.2f} | {ranged(cand, BASE_WEIGHTS, 'low'):.2f}"
              + f" | {ranged(cand, BASE_WEIGHTS, 'high'):.2f} | {cand['confidence']} |")

    print("\n## Sensitivity: winner under different weightings\n")
    print("| Scenario | A | B | C | D | E | Winner |")
    print("|---|---|---|---|---|---|---|")
    for label, w in SCENARIOS.items():
        totals = {n: total(c["score"], w) for n, c in CANDIDATES.items()}
        winner = max(totals, key=totals.get)
        print(f"| {label} | " + " | ".join(f"{v:.2f}" for v in totals.values())
              + f" | {winner.split()[0]} |")

    print("\n## Stress case: A's demand evidence fails (demand = 2) vs B's feasibility improves (= 3)\n")
    a = dict(CANDIDATES["A Robust environments (furniture/fixtures)"]["score"], demand=2)
    b = dict(CANDIDATES["B Staff safety alarms + incident follow-up"]["score"], feasibility=3)
    print(f"A with demand 2: {total(a, BASE_WEIGHTS):.2f}; B with feasibility 3: {total(b, BASE_WEIGHTS):.2f}")
