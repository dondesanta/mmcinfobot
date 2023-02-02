import requests

from parsing.user_agent import header
from parsing.functions.global_pl_info import get_player_global_info


def get_player_info(name):
    link = f'https://minemen.club/player/{name}'
    req = requests.get(link, headers=header).text
    with open('parsing/json/data.json', 'w') as file:
        file.write(req)
        get_player_global_info()
