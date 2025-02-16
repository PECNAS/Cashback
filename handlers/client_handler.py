from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["user"]["start"][1])
async def client_handler(message, state):
	await state.set_state(ClientGroup.CategoryState)
	await message.answer(
			MSGS["choose_category"],
			reply_markup=None
		)

@main_router.message(StateFilter(ClientGroup.CategoryState))
async def CategoryState_handler(message, state):
	category = get_category_by_title(message.text)
	create_client(
		message.from_user.id,
		message.from_user.username,
		category)

	await message.answer(MSGS["client_created_success"])
	await state.clear()