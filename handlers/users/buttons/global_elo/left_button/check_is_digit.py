from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSMs import ClientStatesGroup
from keyboards.ikb_cancel import ikb_cancel
from keyboards.ikb_left_result import ikb_left_result


@dp.message_handler(lambda message: message.text.isdigit(), state=ClientStatesGroup.left)
async def get_result(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        msg_id = data['msg_id']
        number = data['number']
    await message.delete()
    num = int(number) - 1000
    if int(number) >= 1000:
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=f'Global Elo: <b>{number}</b>\n'
                                         f'Elo needed: <b>{str(num*3)}</b>\n'
                                         f'Must have in every mode ≈ <b>{str(num*3/15)}</b>',
                                    reply_markup=ikb_left_result)
        await state.finish()
    else:
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=f'Enter the amount global elo:\n'
                                         f'<em>p.s. global elo 1800 = 1800</em>\n'
                                         f'\n'
                                         f'<em>Please enter a number greater than 1000! ({number})</em>',
                                    reply_markup=ikb_cancel)

