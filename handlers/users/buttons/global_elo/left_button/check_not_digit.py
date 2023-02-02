from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSMs import ClientStatesGroup
from keyboards.ikb_cancel import ikb_cancel


@dp.message_handler(content_types=types.ContentType.ANY, state=ClientStatesGroup.left)
async def check_text_num(message: types.Message, state: FSMContext):
    await message.delete()
    async with state.proxy() as data:
        msg_id = data['msg_id']
    if message.content_type == 'text':
        try:
            if int(message.text) < 0:
                await bot.edit_message_text(chat_id=message.from_user.id,
                                            message_id=msg_id,
                                            text=f'Enter the amount global elo:\n'
                                                 f'<em>p.s. global elo 1800 = 1800</em>\n'
                                                 f'\n'
                                                 f'<em>Please enter a number greater than 1000! ({message.text})</em>',
                                            reply_markup=ikb_cancel)
        except ValueError:
            await bot.edit_message_text(chat_id=message.from_user.id,
                                        message_id=msg_id,
                                        text=f'Enter the amount global elo:\n'
                                             f'<em>p.s. global elo 1800 = 1800</em>\n'
                                             f'\n'
                                             f'<em>Enter the number! ({message.text})</em>',
                                        reply_markup=ikb_cancel)
    else:
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=f'Enter the amount global elo:\n'
                                         f'<em>p.s. global elo 1800 = 1800</em>\n'
                                         f'\n'
                                         f'<em>Enter the number! ({str(message.content_type)})</em>',
                                    reply_markup=ikb_cancel)
