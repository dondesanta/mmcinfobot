from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.ikb_cancel import ikb_cancel
from loader import dp, bot
from FSMs import ClientStatesGroup


@dp.message_handler(content_types=types.ContentType.ANY, state=ClientStatesGroup.find)
async def check_if_not_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        msg_id = data['msg_id']
        if message.content_type != 'text':
            await message.delete()
            await bot.edit_message_text(chat_id=message.from_user.id,
                                        message_id=msg_id,
                                        text=f'<b>Enter nickname</b>:\n'
                                             f'\n'
                                             f'<em>Wrong format! ({str(message.content_type)})</em>',
                                        reply_markup=ikb_cancel)
        else:
            pass
