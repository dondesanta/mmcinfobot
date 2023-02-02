from aiogram import types

from loader import dp, bot
from handlers.users.functions.menu import menu


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.delete()
    x = await bot.send_message(chat_id=message.from_user.id,
                               text='Starting...')
    await menu(message)
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=x.message_id)

