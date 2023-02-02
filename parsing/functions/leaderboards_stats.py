from bs4 import BeautifulSoup
import requests

from parsing.user_agent import header


def lb_stats(NUM):
    # Global result
    link = 'https://minemen.club/leaderboards'
    req = requests.get(link, headers=header).text
    soup = BeautifulSoup(req, 'lxml')
    lb = soup.find_all('table', class_='fl-table')

    lb_find = lb[NUM].find_all('tr')
    result = []
    for i in lb_find[1:]:
        info = i.find_all('td')
        name = i.find('a').text
        if NUM == 1:
            result.append(f'Rank: <code>{info[0].text}</code> Name: <code>{name}</code> Wins: <code>{info[2].text}</code>')
        elif NUM == 2:
            result.append(f'Rank: <code>{info[0].text}</code> Name: <code>{name}</code> Losses: <code>{info[2].text}</code>')
        else:
            result.append(f'Rank: <code>{info[0].text}</code> Name: <code>{name}</code> Elo: <code>{info[2].text}</code>')
    text = '\n'.join(result)
    return text
