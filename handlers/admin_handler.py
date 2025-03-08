from imports import *

@main_router.message(StateFilter(AdminGroup.AdminMenuState), F.text == BUTTONS["admin"]["menu"]["add_cat"])
async def add_cat_handler(message, state):
	await message.answer(
		MSGS["admin_add_cat"],
		reply_markup=getAdminCancelMarkup())
	await state.set_state(AdminGroup.AddCatState)

@main_router.message(StateFilter(AdminGroup.AddCatState))
async def AddCatState_handler(message, state):
	create_category(message.text)

	await message.answer(
		MSGS["admin_add_cat_success"],
		reply_markup=getAdminMarkup())
	await state.set_state(AdminGroup.AdminMenuState)

@main_router.message(StateFilter(AdminGroup.AdminMenuState), F.text == BUTTONS["admin"]["menu"]["remove_cat"])
async def remove_cat_handler(message, state):
	await message.answer(
		MSGS["admin_remove_cat"],
		reply_markup=getCategoriesMarkup())
	await state.set_state(AdminGroup.RemoveCatState)

@main_router.callback_query(StateFilter(AdminGroup.RemoveCatState))
async def RemoveCatState_handler(call, state):
	cat_id = call.data.strip("category_")
	delete_category(cat_id)

	await call.answer()
	await call.message.answer(
			MSGS["admin_remove_cat_success"],
			reply_markup=getAdminMarkup()
		)
	
	await call.message.delete()
	await state.set_state(AdminGroup.AdminMenuState)