from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.ikb_cancel import ikb_cancel
from FSMs import ClientStatesGroup


@dp.callback_query_handler(text='find_button')
async def find_button(callback: types.CallbackQuery, state: FSMContext):
    msg_id = await callback.message.edit_text(text='Enter nickname: ',
                                              reply_markup=ikb_cancel)
    async with state.proxy() as data:
        data['msg_id'] = msg_id.message_id
    await ClientStatesGroup.find.set()
    await callback.answer()
