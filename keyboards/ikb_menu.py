from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton('Find🔎', callback_data='find_button')
                                    ],
                                    [
                                        InlineKeyboardButton('Global Elo', callback_data='global_elo_button')
                                    ],
                                    [
                                        InlineKeyboardButton('Global', callback_data='0'),
                                        InlineKeyboardButton('Wins', callback_data='1'),
                                        InlineKeyboardButton('Losses', callback_data='2')
                                    ],
                                    [
                                        InlineKeyboardButton('NoDebuff', callback_data='3'),
                                        InlineKeyboardButton('Boxing', callback_data='4'),
                                        InlineKeyboardButton('Battlerush', callback_data='5')
                                    ],
                                    [
                                        InlineKeyboardButton('Bridges', callback_data='6'),
                                        InlineKeyboardButton('BedFight', callback_data='7'),
                                        InlineKeyboardButton('Sumo', callback_data='8')
                                    ],
                                    [
                                        InlineKeyboardButton('Pearlfight', callback_data='9'),
                                        InlineKeyboardButton('BuildUHC', callback_data='10'),
                                        InlineKeyboardButton('SkyWars', callback_data='11')
                                    ],
                                    [
                                        InlineKeyboardButton('Classic', callback_data='12'),
                                        InlineKeyboardButton('FinalUHC', callback_data='13'),
                                        InlineKeyboardButton('Invaded', callback_data='14')
                                    ],
                                    [
                                        InlineKeyboardButton('Archer', callback_data='15'),
                                        InlineKeyboardButton('Debuff', callback_data='16'),
                                        InlineKeyboardButton('Soup', callback_data='17')
                                    ]
                                ])
