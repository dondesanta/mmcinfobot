from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSMs import ClientStatesGroup
from keyboards.ikb_cancel import ikb_cancel


@dp.message_handler(content_types=types.ContentType.ANY, state=ClientStatesGroup.calculate)
async def check_text_num(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        msg_id = data['msg_id']
    if message.content_type == 'text':
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=f'Enter the number of elo from ALL modes:\n'
                                         f'<em>p.s. example: nodebuff - 1400 elo, sumo - 1500 elo = 900 elo</em>\n'
                                         f'\n'
                                         f'<em>Enter the number! ({message.text})</em>',
                                    reply_markup=ikb_cancel)
    else:
        await bot.edit_message_text(
            chat_id=message.from_user.id,
            message_id=msg_id,
            text=f'Enter the number of elo from ALL modes:\n'
                 f'<em>p.s. example: nodebuff - 1400 elo, sumo - 1500 elo = 900 elo</em>\n'
                 f'\n'
                 f'<em>Enter the number! ({str(message.content_type)})</em>',
            reply_markup=ikb_cancel)
