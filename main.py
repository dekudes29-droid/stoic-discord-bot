import random
import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

quotes = [
    ("Waste no more time arguing what a good man should be. Be one.", "Marcus Aurelius"),
    ("We suffer more often in imagination than in reality.", "Seneca"),
    ("It's not what happens to you, but how you react to it that matters.", "Epictetus"),
    ("You have power over your mind—not outside events. Realize this, and you will find strength.", "Marcus Aurelius"),
    ("Difficulties strengthen the mind, as labor does the body.", "Seneca"),
]

quote, author = random.choice(quotes)

payload = {
    "embeds": [
        {
            "title": "🏛️ Stoic Quote of the Day",
            "description": f"*{quote}*",
            "color": 0xB8860B,
            "footer": {
                "text": author
            }
        }
    ]
}

requests.post(WEBHOOK, json=payload)
