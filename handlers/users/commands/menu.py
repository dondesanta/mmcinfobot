from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from handlers.users.functions.menu import menu


@dp.message_handler(commands=['menu'], state='*')
async def menu_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await menu(message)
