import requests
from datetime import datetime

def send_discord_webhook(webhook_url, sender, title, body):

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().strftime("%y")
    current_time = datetime.now().strftime("%H:%M:%S")


    embed = {
        "title": f"{title}  --  {day}/{month}/{year}",
        "description": body,
        "footer": {"text": f"From {sender}"},
        "timestamp": datetime.now().isoformat(),
        "color": 0xfccc04
    }

    payload = {
        "embeds": [embed]
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Webhook sent successfully!")
    else:
        print(f"Failed to send webhook. Status code: {response.status_code}")
        print(response.text)
