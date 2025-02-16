from imports import *

@main_router.message(StateFilter(None), Command(commands=["start"]))
async def command_start_handler(message, state):
	res = check_user(message.from_user.id)

	if res == None:
		await message.answer(
			MSGS["start_message__no_reg"],
			reply_markup=getUsersStartMarkup())
	else:
		if res["role"] == "client":
			await message.answer(
			MSGS["start_message__client"],
			reply_markup=None)
		elif res["role"] == "seller":
			await message.answer(
			MSGS["start_message__seller"],
			reply_markup=None)

@main_router.message(F.text == BUTTONS["user"]["cancel"]) # отмена для пользователей
async def cancel_handler(message, state):
	await state.clear()
	await message.answer(
		MSGS["canceled"],
		reply_markup=getUsersStartMarkup())