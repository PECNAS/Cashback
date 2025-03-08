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
			reply_markup=getSellerMarkup())

@main_router.message(StateFilter(None), Command(commands=["admin"]))
async def command_admin_handler(message, state):
	await message.answer(
		MSGS["admin_menu_start"],
		reply_markup=getAdminMarkup())
	await state.set_state(AdminGroup.AdminMenuState)

@main_router.message(F.text == BUTTONS["user"]["cancel"]) # отмена для пользователей
async def cancel_handler(message, state):
	await state.clear()
	await message.answer(
		MSGS["cancelled"],
		reply_markup=getUsersStartMarkup())

@main_router.message(F.text == BUTTONS["admin"]["cancel"])
async def admin_cancel_handler(message, state):
	await state.set_state(AdminGroup.AdminMenuState)
	await message.answer(
		MSGS["cancelled"],
		reply_markup=getAdminMarkup())