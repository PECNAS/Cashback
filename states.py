from aiogram.fsm.state import StatesGroup, State

class ClientGroup(StatesGroup):
	CategoryState = State()

class SellerGroup(StatesGroup):
	ShopTitleState = State()
	ShopUrlState = State()