from bs4 import BeautifulSoup
import requests

from parsing.user_agent import header
from data.config import gamemodes


def lb_more_check(gamemode, num_list=1):
    # More global result
    error_text = '<b>Website Error: 500 "Something went wrong</b>"'
    link = f'https://minemen.club/leaderboards/practice/{gamemodes[str(gamemode)]}/{num_list}'
    req = requests.get(link, headers=header).text
    soup = BeautifulSoup(req, 'lxml')
    if soup.find('p') is not None:
        return error_text
    else:
        lb_info = soup.find_all('tr')
        lb_stats_more = []
        for i in lb_info[1:]:
            info = i.find_all('td')
            name = i.find('a').text
            if int(gamemode) == 1:
                lb_stats_more.append(f'Rank: <code>#{info[0].text}</code> Name: <code>{name}</code> Wins: <code>{info[2].text}</code>')
            elif int(gamemode) == 2:
                lb_stats_more.append(f'Rank: <code>#{info[0].text}</code> Name: <code>{name}</code> Losses: <code>{info[2].text}</code>')
            else:
                lb_stats_more.append(f'Rank: <code>#{info[0].text}</code> Name: <code>{name}</code> Elo: <code>{info[2].text}</code>')
        lb_more_text = '\n'.join(lb_stats_more)
        return lb_more_text
