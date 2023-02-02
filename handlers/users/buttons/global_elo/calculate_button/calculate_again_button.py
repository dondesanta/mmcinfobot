from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.buttons.global_elo.calculate_button.calculate_button import calculate_button
from loader import dp


@dp.callback_query_handler(text='calculate_again_button')
async def calculate_again_button(callback: types.CallbackQuery, state: FSMContext):
    await calculate_button(callback, state)
    await callback.answer()
