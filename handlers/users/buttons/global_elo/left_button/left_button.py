from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from FSMs import ClientStatesGroup
from keyboards.ikb_cancel import ikb_cancel


@dp.callback_query_handler(text='left_button')
async def left_button(callback: types.CallbackQuery, state: FSMContext):
    msg_id = await callback.message.edit_text(text='Enter the amount global elo:\n'
                                                   '<em>p.s. global elo 1800 = 1800</em>',
                                              reply_markup=ikb_cancel)
    async with state.proxy() as data:
        data['msg_id'] = msg_id.message_id
    await ClientStatesGroup.left.set()
    await callback.answer()
