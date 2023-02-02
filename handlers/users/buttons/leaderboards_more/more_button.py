from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from parsing.functions.leaderboards_stats_more import lb_more_check
from keyboards.ikb_lb_stats_more import ikb_stats_more


@dp.callback_query_handler(text='more_button')
async def more_button(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['page'] = 1
        button_num = data['button_num']
    i = 0
    result = []
    while i < 20:
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
                                     reply_markup=ikb_stats_more)
    await callback.message.edit_text(text=lb_more_check(button_num, data['page']),
                                     reply_markup=ikb_stats_more)
    await callback.answer()
