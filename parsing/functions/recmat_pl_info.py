from datetime import datetime

from bs4 import BeautifulSoup


def rec_matches(name):
    with open('parsing/json/data.json') as file:
        soup = BeautifulSoup(file, 'lxml')
        file.read()

    player = soup.find('div', class_='player-info-name-upper')
    player_name_and_rank = player.find_all('span')
    player_name = player_name_and_rank[0].text
    rank = player_name_and_rank[1].text

    recent_matches = soup.find('div', class_='recent-matches-holder')
    try:
        recent_match = recent_matches.find_all('div', class_='recent-match-holder')
    except AttributeError:
        text = f'<b>{player_name}</b> [{rank}]\n' \
               '<b>Error:</b>\n' \
               '\n' \
               '<em>Recent matches not found</em>'
        return text

    result = []
    for i in recent_match:
        player1 = i.find('div', class_='player-1').find('div', class_='player-info')
        player1_stats = player1.find_all('span')
        player1_name = player1_stats[0].text.strip()
        player1_elo = player1_stats[1].text.strip()[:-5].strip()
        player1_elo_remove = player1_stats[2].text.strip()

        player2 = i.find('div', class_='player-2').find('div', class_='player-info')
        player2_name = player2.find(class_='name').text

        recent_match_type = i.find('div', class_='recent-match-type')
        match_type = recent_match_type.find('span', class_='match-type').text
        match_datetime = recent_match_type.find('time').get('datetime').replace('T', ' ')[:-1]
        date1 = datetime.strptime(match_datetime, "%Y-%m-%d %H:%M:%S")
        delta = datetime.utcnow() - date1
        timeresult = delta.total_seconds()
        if timeresult / 60 / 60 <= 24:
            status = f'{round(timeresult / 60 / 60)} hours ago'
        elif timeresult / 60 / 60 >= 24:
            status = f'{round(timeresult / 60 / 60 / 24)} days ago'

        result.append(f'<b>{player1_name}</b> vs <b>{player2_name}</b>\n└ {match_type} | {player1_elo} {player1_elo_remove} | {status}')
    result_text = "\n".join(result)
    text = f'<b>{player_name}</b> [{rank}]\n' \
           f'<code>Recent Matches:</code>\n' \
           f'{result_text}'

    return text
