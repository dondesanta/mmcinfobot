from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.ikb_menu import ikb_menu
from parsing.functions.online import online


@dp.callback_query_handler(text='menu_back_button', state='*')
async def main_back_button(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback.message.edit_text(text=f'<b>Welcome, {callback.from_user.username}!</b>'
                                          f'\nCurrent online: <i>loading...</i>'
                                          f'\nChoose a category👇',
                                     reply_markup=ikb_menu)
    await callback.message.edit_text(text=f'<b>Welcome, {callback.from_user.username}!</b>'
                                          f'\nCurrent online: <b>{online()}</b>'
                                          f'\nChoose a category👇',
                                     reply_markup=ikb_menu)
    await callback.answer()
