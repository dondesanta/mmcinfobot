from aiogram import types
from aiogram.dispatcher import FSMContext

from FSMs import ClientStatesGroup
from keyboards.ikb_find import ikb_find
from loader import dp
from parsing.functions.global_pl_info import get_player_global_info


@dp.callback_query_handler(text='global_find_button', state=ClientStatesGroup.find)
async def global_find_button(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num_find = data['num_find']
        if num_find != 1:
            await callback.message.edit_text(text=get_player_global_info(),
                                             reply_markup=ikb_find(data['ign']))
            data['num_find'] = 1
            await callback.answer()
        else:
            await callback.answer('You are already on this page!')
