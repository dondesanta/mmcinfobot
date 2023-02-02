import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admin_id = [
    827285005
]

button_num = [0]

gamemodes = {
    '0': "topelo",
    '1': "topwins",
    '2': "toplosses",
    '3': "nodebuff",
    '4': "boxing",
    '5': "battlerush",
    '6': "bridges",
    '7': "bedfight",
    '8': "sumo",
    '9': "pearlfight",
    '10': "builduhc",
    '11': "skywars",
    '12': "classic",
    '13': "finaluhc",
    '14': "invaded",
    '15': "archer",
    '16': "debuff",
    '17': "soup"
}
