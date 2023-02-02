import requests

from parsing.user_agent import header


def online():
    link = 'https://api.mcstatus.io/v2/status/java/eu.minemen.club'
    req = requests.get(link, headers=header)
    online_text = req.json()["players"]["online"]
    return online_text
