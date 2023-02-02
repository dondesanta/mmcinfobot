from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from parsing.functions.leaderboards_stats import lb_stats
from keyboards.ikb_lb_stats import ikb_lb_stats


@dp.callback_query_handler(text='back_button')
async def back_button(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        button_num = data['button_num']
    i = 0
    result = []
    while i < 10:
        i += 1
        NUM = int(button_num)
        if NUM == 1:
            result.append(
                f'Rank: <code>#{i}</code> Name: <code>#########</code> Wins: <code>####</code>')
        elif NUM == 2:
            result.append(
                f'Rank: <code>#{i}</code> Name: <code>#########</code> Losses: <code>####</code>')
        else:
            result.append(
                f'Rank: <code>#{i}</code> Name: <code>#########</code> Elo: <code>####</code>')
    text = '\n'.join(result)
    await callback.message.edit_text(text=text,
                                     reply_markup=ikb_lb_stats(button_num))
    await callback.message.edit_text(text=lb_stats(int(button_num)),
                                     reply_markup=ikb_lb_stats(button_num))
    await callback.answer()
