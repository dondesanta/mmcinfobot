from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from FSMs import ClientStatesGroup
from handlers.users.buttons.find.find_button import find_button


@dp.callback_query_handler(text='find_again_button', state=ClientStatesGroup.find)
async def find_again_button(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await find_button(callback, state)
    await callback.answer()
