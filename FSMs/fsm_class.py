from aiogram.dispatcher.filters.state import StatesGroup, State


class ClientStatesGroup(StatesGroup):
    calculate = State()
    left = State()
    find = State()

class PaginationButtons(StatesGroup):
    pagination_more = State()