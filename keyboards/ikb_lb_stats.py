from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import gamemodes


def ikb_lb_stats(num):
    ikb_lb_stats = InlineKeyboardMarkup(row_width=3,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton('<= Back', callback_data='menu_back_button'),
                                                InlineKeyboardButton('More...', callback_data='more_button'),
                                                InlineKeyboardButton('Link', callback_data='link_button',
                                                                     url=f'https://minemen.club/leaderboards/practice/'
                                                                         f'{gamemodes[num]}/1')
                                            ]
                                        ])
    return ikb_lb_stats
