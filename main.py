import random
import os
import json
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

# Load quotes from quotes.json
with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

selected = random.choice(quotes)

quote = selected["quote"]
author = selected["author"]

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

response = requests.post(WEBHOOK, json=payload)

if response.status_code == 204:
    print("Quote sent successfully!")
else:
    print(f"Failed: {response.status_code}")
    print(response.text)
