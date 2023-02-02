from bs4 import BeautifulSoup


def practice(name):
    with open('parsing/json/data.json') as file:
        soup = BeautifulSoup(file, 'lxml')
        file.read()

    player = soup.find('div', class_='player-info-name-upper')
    player_name_and_rank = player.find_all('span')
    player_name = player_name_and_rank[0].text
    rank = player_name_and_rank[1].text

    statistics_get = soup.find_all('div', class_='tab-content')
    statistics = statistics_get[1].find_all('div', class_='statistics-practice')
    elo_result = []
    statistics_result = []
    for x in statistics:
        title = x.find('span', class_='title').text
        stats = x.find_all('span', class_='stat-tab')
        elo = stats[0].find(class_='number').text
        wins = stats[1].find(class_='number').text
        losses = stats[2].find(class_='number').text
        wl_ratio = stats[3].find(class_='number').text
        elo_result.append(int(elo.replace(',', '')))
        statistics_result.append(f'├ <b>{title}</b> - {elo} / {wins} / {losses} / {wl_ratio}')
    sum_elo = sum(elo_result) - 15000
    statistics = "\n".join(statistics_result)

    text = f'<b>{player_name}</b> [{rank}]\n' \
           f'<code>(Elo / Wins / Losses / WL Ratio)</code>\n' \
           f'{statistics}\n' \
           f'└ <b>Total elo from all modes</b>: {sum_elo}'

    return text
