from datetime import datetime

from bs4 import BeautifulSoup


def get_player_global_info():
    with open('parsing/json/data.json', 'r') as file:
        soup = BeautifulSoup(file, 'lxml')
        file.read()

    # Name + rank
    player = soup.find('div', class_='player-info-name-upper')
    if player is None:
        ign_nf = 'Player not found!'
        return ign_nf
    else:
        player_name_and_rank = player.find_all('span')
        player_name = player_name_and_rank[0].text
        rank = player_name_and_rank[1].text


        # Status
        find_time_ago = soup.find('span', class_='player-status offline')
        check_ban = soup.find('span', class_='player-status banned')
        check_online = soup.find('span', class_='player-status online')
        if find_time_ago is None:
            if check_online is None:
                if check_ban is None:
                    status = '-'
                else:
                    status = 'This user is currently banned'
            else:
                status = check_online.text.strip()
        else:
            get_time = find_time_ago.find('time').get('datetime').replace('T', ' ')
            time_get = get_time[:-5]
            date1 = datetime.strptime(time_get, "%Y-%m-%d %H:%M:%S")
            delta = datetime.utcnow() - date1
            timeresult = delta.total_seconds()
            if timeresult / 60 / 60 <= 24:
                status = f'Last online {round(timeresult/60/60)} hours ago'
            elif timeresult / 60 / 60 >= 24:
                status = f'Last online {round(timeresult/60/60/24)} days ago'


        # First joined
        first_joined_find = soup.find('table', class_='general-info fl-table').find_all('td')
        date = datetime.strptime(first_joined_find[1].text, "%d-%m-%Y")
        delta = datetime.utcnow() - date
        timeresult_fj = delta.total_seconds()/60/60/24

        # Practice stats
        practice_stats_find = soup.find_all('div', class_='statistics-practice')
        practice_stats = practice_stats_find[0].find_all(class_='stat-tab')
        result = []
        for i in practice_stats:
            result.append(i.find(class_='number').text)


        # Achievement
        achievements = soup.find('div', class_='player-info-achievements')
        if achievements is None:
            achievement = '-'
        else:
            all_achievements = achievements.find_all('div', class_='achievement')
            achievement = []
            for i in all_achievements:
                name = i.find('div', class_='achievement-title').text.strip()
                achievement.append(name)
            achievement = ', '.join(achievement)

        # Message
        text = f'<b>{player_name}</b> [{rank}]\n' \
               f'<b>Status</b>: <em>{status}</em>\n' \
               f'<b>First joined</b>: <em>{first_joined_find[1].text} ({int(timeresult_fj)} days from now)</em>\n' \
               f'<b>Practice (Global Elo | W | L | W/L Ratio)</b>:\n' \
               f'└ <code><em>{result[0]} / {result[1]} / {result[2]} / {result[3]}\n</em></code>' \
               f'<b>Achievements</b>: <em>{achievement}</em>'


        return text

