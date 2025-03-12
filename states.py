from aiogram.fsm.state import StatesGroup, State

class ClientGroup(StatesGroup):
	CategoryState = State()
	MinCashbackState = State()

class SellerGroup(StatesGroup):
	ShopTitleState = State()
	ShopUrlState = State()
	EditItemState = State()
	EditParameterState = State()

class CreateItemGroup(StatesGroup):
	ItemTitleState = State()
	ItemDescState = State()
	ItemImageState = State()
	ItemPriceState = State()
	ItemLinkState = State()
	ItemCashbackState = State()
	ItemConditionState = State()
	ItemCategoryState = State()
	ItemConfirmState = State()

class AdminGroup(StatesGroup):
	AdminMenuState = State()
	AddCatState = State()
	RemoveCatState = State()
	AddModerState = State()
	RemoveModerState = State()

class ShowItemsGroup(StatesGroup):
	CategoryState = State()
	ItemsListState = State()