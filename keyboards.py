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
	for data, btn in BUTTONS["seller"]["items_list"].items():
		builder.button(
			text=btn,
			callback_data=f"{data}{item.id}|{item.title}")
	builder.button(
		text="Ссылка",
		url=item.link)
	builder.button(
		text="Назад ⏪",
		callback_data=f"back")

	builder.adjust(2)
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

def getClientMarkup():
	builder = ReplyKeyboardBuilder()
	for btn in BUTTONS["client"]["menu"].values():
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

def getClientMenuMarkup(link):
	builder = InlineKeyboardBuilder()
	for data, btn in BUTTONS["client"]["items_list"].items():
		if data == "buy":
			builder.button(
				text=btn,
				url=link)
		else:
			builder.button(
				text=btn,
				callback_data=data)

	builder.adjust(3)
	markup = builder.as_markup()

	return markup

def getModerMarkup():
	builder = ReplyKeyboardBuilder()
	for btn in BUTTONS["moder"]["menu"].values():
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup

def getCloseRequestMarkup(req_id):
	builder = InlineKeyboardBuilder()
	for data, btn in BUTTONS["moder"]["close_req"].items():
		builder.button(
			text=btn,
			callback_data=f"{data}__{req_id}")

	return builder.as_markup()

def getSendItemMarkup(link, item_id):
	builder = InlineKeyboardBuilder()
	builder.button(
		text=BUTTONS["client"]["items_list"]["buy"],
		url=link)
	builder.button(
		text=BUTTONS["client"]["items_list"]["check"],
		callback_data=f"check_new__{item_id}")

	return builder.as_markup()

def getItemEditMarkup():
	builder = InlineKeyboardBuilder()
	for data, btn in BUTTONS["seller"]["edit_item"].items():
		builder.button(
			text=btn,
			callback_data=data)

	builder.adjust(2)
	return builder.as_markup()

if __name__ == "__main__":
	getCategoriesMarkup()