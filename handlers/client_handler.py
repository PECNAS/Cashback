from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["user"]["start"][1])
async def client_handler(message, state):
	await state.set_state(ClientGroup.CategoryState)
	await message.answer(
			MSGS["choose_category"],
			reply_markup=getCategoriesMarkup()
		)

@main_router.callback_query(StateFilter(ClientGroup.CategoryState))
async def CategoryState_handler(call, state):
	category = get_category_by_id(call.data.strip("category_"))
	create_client(
		call.from_user.id,
		call.from_user.username,
		category)

	await call.answer()
	await call.message.answer(
		MSGS["client_created_success"],
		reply_markup=getClientMarkup())
	await state.clear()