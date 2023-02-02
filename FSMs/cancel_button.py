from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.ikb_global_elo import ikb_global_elo
from parsing.functions.online import online
from keyboards.ikb_menu import ikb_menu


@dp.callback_query_handler(text='cancel_button', state='*')
async def cancel_button(callback: types.CallbackQuery, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is None:
        return
    elif cur_state == 'ClientStatesGroup:calculate' or cur_state == 'ClientStatesGroup:left':
        await callback.message.edit_text(text='<b>Calculate</b> - determine how much global elo will be\n'
                                              '<b>Left</b> - calculate how much elo is left before',
                                         reply_markup=ikb_global_elo,
                                         parse_mode='HTML')
    elif cur_state == 'ClientStatesGroup:find':
        await callback.message.edit_text(text=f'<b>Welcome, {callback.from_user.username}</b>\n'
                                              f'Current online: <i>loading...</i>'
                                              f'\nChoose a category👇',
                                         reply_markup=ikb_menu)
        await callback.message.edit_text(text=f'<b>Welcome, {callback.from_user.username}</b>\n'
                                              f'Current online: <b>{online()}</b>'
                                              f'\nChoose a category👇',
                                         reply_markup=ikb_menu)
    await state.finish()
    await callback.answer()
