from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_stats_more = InlineKeyboardMarkup(row_width=3,
                           inline_keyboard=[
                               [
                                    InlineKeyboardButton('<= Previous', callback_data='previous_button'),
                                    InlineKeyboardButton('Back', callback_data='back_button'),
                                    InlineKeyboardButton('Next =>', callback_data='next_button')
                               ]
                           ])
