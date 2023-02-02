from aiogram import types

from loader import bot
from parsing.functions.online import online
from keyboards.ikb_menu import ikb_menu


async def menu(message: types.Message):
    x = await bot.send_message(chat_id=message.from_user.id,
                               text=f'<b>Welcome, {message.from_user.username}!</b>'
                                    f'\nCurrent online: <i>loading...</i>'
                                    f'\nChoose a category👇',
                               reply_markup=ikb_menu)
    await bot.edit_message_text(chat_id=message.from_user.id,
                                message_id=x.message_id,
                                text=f'<b>Welcome, {message.from_user.username}!</b>'
                                     f'\nCurrent online: <b>{online()}</b>'
                                     f'\nChoose a category👇',
                                reply_markup=ikb_menu)

