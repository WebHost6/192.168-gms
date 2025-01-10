import requests
from datetime import datetime

# Discord webhook URL
WEBHOOK_URL = "YOUR_WEBHOOK_URL"

# Variables
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
current_time = datetime.now().strftime("%H:%M:%S")
sender = "Your Name or Identifier"
title = "Your Embed Title"
body = "This is the body content of the embed."

# Embed data
embed = {
    "title": f"{title}  --  {day}/{month}/{year}",
    "description": body,
    "footer": {"text": f"From {sender}"},
    "timestamp": datetime.now().isoformat(),
    "color": 0xfccc04  # Embed color in hexadecimal
}

# Payload for the webhook
payload = {
    "embeds": [embed]
}

# Sending the webhook
response = requests.post(WEBHOOK_URL, json=payload)

# Check the response
if response.status_code == 204:
    print("Webhook sent successfully!")
else:
    print(f"Failed to send webhook. Status code: {response.status_code}")
    print(response.text)
