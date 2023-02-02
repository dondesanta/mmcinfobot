from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from handlers.users.functions.pagination_more import pagination_more


@dp.callback_query_handler(text='previous_button')
async def previous_button(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['page'] -= 1
        if data['page'] > 0:
            await callback.answer(str(data['page']))
            await pagination_more(callback, state, data['page'])
        else:
            data['page'] = 25
            await callback.answer(str(data['page']))
            await pagination_more(callback, state, data['page'])
