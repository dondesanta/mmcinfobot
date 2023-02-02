from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.ikb_cancel import ikb_cancel
from FSMs import ClientStatesGroup


@dp.callback_query_handler(text='calculate_button')
async def calculate_button(callback: types.CallbackQuery, state: FSMContext):
    msg_id = await callback.message.edit_text(text='Enter the number of elo from ALL modes:\n'
                                                   '<em>p.s. example: nodebuff - 1400 elo, sumo - 1500 elo = 900 elo</em>',
                                              reply_markup=ikb_cancel)
    async with state.proxy() as data:
        data['msg_id'] = msg_id.message_id
    await ClientStatesGroup.calculate.set()
    await callback.answer()
