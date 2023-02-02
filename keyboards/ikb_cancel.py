from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_cancel = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton('Cancel', callback_data='cancel_button')
                                      ]
                                  ])
