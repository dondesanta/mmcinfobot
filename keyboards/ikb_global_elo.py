from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_global_elo = InlineKeyboardMarkup(row_width=3,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton('Left', callback_data='left_button'),
                                              InlineKeyboardButton('Calculate', callback_data='calculate_button')
                                          ],
                                          [
                                              InlineKeyboardButton('<= Back', callback_data='menu_back_button')
                                          ]
                                      ])
