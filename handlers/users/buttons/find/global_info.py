from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSMs import ClientStatesGroup
from parsing.functions.get_pl_page import get_player_info
from parsing.functions.global_pl_info import get_player_global_info
from keyboards.ikb_cancel import ikb_cancel
from keyboards.ikb_find import ikb_find


@dp.message_handler(content_types=types.ContentType.TEXT, state=ClientStatesGroup.find)
async def get_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ign'] = message.text
        data['num_find'] = 1
        msg_id = data['msg_id']
    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=msg_id,
                                text='Loading...')
    get_player_info(data['ign'])
    text = get_player_global_info()
    if text == 'Player not found!':
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=msg_id,
                                    text=f'<b>Enter nickname</b>:\n'
                                         f'\n'
                                         f'<em>Player not found!</em>',
                                    reply_markup=ikb_cancel)
    else:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=msg_id,
                                    text=text,
                                    reply_markup=ikb_find(data['ign']))
