import requests


def get_perspective_toxicity_scores(dialogue_outputs):
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

    categories = [
        "toxicity",
        "obscene",
        "insult",
        "identity_attack",
        "threat",
        "severe_toxicity",
    ]
    scores = {category: [] for category in categories}

    for output in dialogue_outputs:
        data = {
            "comment": {"text": output},
            "languages": ["en"],
            "requestedAttributes": {
                "TOXICITY": {},
                "SEVERE_TOXICITY": {},
                "OBSCENE": {},
                "INSULT": {},
                "IDENTITY_ATTACK": {},
                "THREAT": {},
            },
        }
        params = {"key": ""}
        response = requests.post(url, json=data, params=params)

        if response.status_code == 200:
            results = response.json()["attributeScores"]
            for k, v in results.items():
                scores[k.lower()].append(v["summaryScore"]["value"])
        else:
            print("Error:", response.status_code, response.text)
            break

    return scores


dialogue_outputs = [
    """Seized Rainbow Hats Trigger Global Backlash: FIFA and Qatar Face LGBTQ+ Rights Reckoning. The bans have sparked global protests, social media outrage, and calls for action by governments and sponsors. This clash shows cultural conservatism colliding with calls for inclusivity."""
]
print(get_perspective_toxicity_scores(dialogue_outputs))
