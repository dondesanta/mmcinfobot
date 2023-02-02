from aiogram import types
from aiogram.dispatcher import FSMContext

from FSMs import ClientStatesGroup
from keyboards.ikb_find import ikb_find
from loader import dp
from parsing.functions.practice_pl_info import practice


@dp.callback_query_handler(text='practice_find_button', state=ClientStatesGroup.find)
async def practice_find_button(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num_find = data['num_find']
        if num_find != 2:
            await callback.message.edit_text(text=practice(data['ign']),
                                             reply_markup=ikb_find(data['ign']))
            data['num_find'] = 2
            await callback.answer()
        else:
            await callback.answer('You are already on this page!')
