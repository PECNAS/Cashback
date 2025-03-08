from aiogram.fsm.state import StatesGroup, State

class ClientGroup(StatesGroup):
	CategoryState = State()

class SellerGroup(StatesGroup):
	ShopTitleState = State()
	ShopUrlState = State()

class CreateItemGroup(StatesGroup):
	ItemTitleState = State()
	ItemDescState = State()
	ItemImageState = State()
	ItemPriceState = State()
	ItemCashbackState = State()
	ItemConditionState = State()
	ItemCategoryState = State()
	ItemConfirmState = State()

class AdminGroup(StatesGroup):
	AdminMenuState = State()
	AddCatState = State()
	RemoveCatState = State()