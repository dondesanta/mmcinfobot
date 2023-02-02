from aiogram import types
from aiogram.dispatcher import FSMContext

from parsing.functions.leaderboards_stats_more import lb_more_check
from keyboards.ikb_lb_stats_more import ikb_stats_more


async def pagination_more(callback: types.CallbackQuery, state: FSMContext, num):
    async with state.proxy() as data:
        button_num = data['button_num']
    await callback.message.edit_text(text=lb_more_check(button_num, num),
                                     reply_markup=ikb_stats_more)
