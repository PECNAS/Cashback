from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import BUTTONS
from database import get_categories

def getUsersStartMarkup():
	builder = ReplyKeyboardBuilder()

	for btn in BUTTONS["user"]["start"]:
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

def getCategoriesMarkup():
	builder = InlineKeyboardBuilder()

	for cat in get_categories():
		builder.button(
			callback_data=f"category_{cat.id}",
			text=cat.title)

	builder.adjust(2)
	markup = builder.as_markup()

	return markup

def getConfirmMarkup():
	builder = InlineKeyboardBuilder()

	for k, v in BUTTONS["seller"]["confirm"].items():
		builder.button(
			callback_data=k,
			text=v)

	builder.adjust(2)
	markup = builder.as_markup()

	return markup

def getSellerMarkup():
	builder = ReplyKeyboardBuilder()

	for btn in BUTTONS["seller"]["menu"]:
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

def getSellerItemsMarkup(items):
	builder = InlineKeyboardBuilder()

	for item in items:
		builder.button(
			text=item.title,
			callback_data=f"item_{item.id}")

	builder.adjust(2)
	markup = builder.as_markup()

	return markup

def getDeleteItemMarkup(item):
	builder = InlineKeyboardBuilder()
	builder.button(
		text="Удалить 🗑",
		callback_data=f"remove_item__{item.id}|{item.title}")
	return builder.as_markup()

def getAdminMarkup():
	builder = ReplyKeyboardBuilder()

	for btn in BUTTONS["admin"]["menu"].values():
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

def getAdminCancelMarkup():
	builder = ReplyKeyboardBuilder()
	builder.button(text=BUTTONS["admin"]["cancel"])

	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

if __name__ == "__main__":
	getCategoriesMarkup()