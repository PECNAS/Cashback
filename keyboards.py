from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import BUTTONS

def getUsersStartMarkup():
	builder = ReplyKeyboardBuilder()

	for btn in BUTTONS["user"]["start"]:
		builder.button(text=btn)

	builder.adjust(2)
	markup = builder.as_markup()
	markup.resize_keyboard = True

	return markup