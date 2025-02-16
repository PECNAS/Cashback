from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["user"]["start"][0])
async def seller_handler(message, state):
	await message.answer(MSGS["seller_shop_title"])
	await state.set_state(SellerGroup.ShopTitleState)

@main_router.message(StateFilter(SellerGroup.ShopTitleState))
async def ShopTitleState_handler(message, state):
	await state.update_data(title=message.text)
	await message.answer(MSGS["seller_shop_url"])
	await state.set_state(SellerGroup.ShopUrlState)

@main_router.message(StateFilter(SellerGroup.ShopUrlState))
async def ShopUrlState_handler(message, state):
	shop_title = (await state.get_data()).get("title")
	create_seller(
		message.from_user.id,
		message.from_user.username,
		shop_title,
		message.text)

	await message.answer(MSGS["seller_created_success"])

