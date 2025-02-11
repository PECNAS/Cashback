from imports import *

@main_router.message(StateFilter(None), Command(commands=["start"]))
async def command_start_handler(message, state):
	await message.answer(
		MSGS["start_message"],
		reply_markup=getUsersStartMarkup())

@main_router.message(F.text == BUTTONS["user"]["cancel"]) # отмена для пользователей
async def cancel_handler(message, state):
	await state.clear()
	await message.answer(
		MSGS["canceled"],
		reply_markup=getUsersStartMarkup())