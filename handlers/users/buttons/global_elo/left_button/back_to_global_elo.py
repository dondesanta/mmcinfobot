from aiogram import types

from loader import dp
from keyboards.ikb_global_elo import ikb_global_elo


@dp.callback_query_handler(text='back_to_globalelo_from_left_button')
async def back_to_global_elo(callback: types.CallbackQuery):
    await callback.message.edit_text(text='<b>Left</b> - calculate how much elo is left before\n'
                                          '<b>Calculate</b> - determine how much global elo will be',
                                     reply_markup=ikb_global_elo)
    await callback.answer()