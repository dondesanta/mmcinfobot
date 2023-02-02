from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_left_result = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton('<= Back', callback_data='back_to_globalelo_from_left_button'),
                                               InlineKeyboardButton('Calculate', callback_data='calculate_again_left_button')
                                           ]
                                       ])
