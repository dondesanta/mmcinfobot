from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from FSMs import ClientStatesGroup
from keyboards.ikb_calculate_result import ikb_calculate_result


@dp.message_handler(lambda message: message.text.isdigit(), state=ClientStatesGroup.calculate)
async def load_num(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        number = data['number']
        msg_id = data['msg_id']
    num = round(int(data['number']) / 3) + 1000
    await message.delete()
    await bot.edit_message_text(chat_id=message.from_user.id,
                                message_id=msg_id,
                                text=f'All mode elo: <b>{str(number)}</b>\nGlobal Elo: <b>{str(num)}</b>',
                                reply_markup=ikb_calculate_result)
    await state.finish()
