from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ikb_calculate_result = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton('<= Back', callback_data='back_to_globalelo_button'),
                                                    InlineKeyboardButton('Calculate', callback_data='calculate_again_button')
                                                ]
                                            ])
