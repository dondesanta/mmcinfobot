from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb_find(name):
    ikb = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton('Global', callback_data='global_find_button'),
                                       InlineKeyboardButton('Practice', callback_data='practice_find_button'),
                                       InlineKeyboardButton('R. Matches', callback_data='recent_matches_find_button')
                                   ],
                                   [
                                       InlineKeyboardButton('NameMC', url=f'https://ru.namemc.com/profile/{name}')
                                   ],
                                   [
                                       InlineKeyboardButton('<= Back', callback_data='menu_back_button'),
                                       InlineKeyboardButton('Find🔎', callback_data='find_again_button')
                                   ]
                               ])
    return ikb
