from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.buttons.global_elo.left_button.left_button import left_button
from loader import dp
from FSMs import ClientStatesGroup


@dp.callback_query_handler(text='calculate_again_left_button')
async def calculate_again_button(callback: types.CallbackQuery, state: FSMContext):
    await left_button(callback, state)
    await ClientStatesGroup.left.set()
    await callback.answer()
