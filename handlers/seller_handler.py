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

	await message.answer(
			MSGS["seller_created_success"],
			reply_markup=getSellerMarkup()
		)

	await state.clear()

@main_router.message(StateFilter(None), F.text == BUTTONS["seller"]["menu"][0])
async def add_item_handler(message, state):
	await message.answer(MSGS["seller_add_item__0"])

	await state.set_state(CreateItemGroup.ItemTitleState)

@main_router.message(StateFilter(CreateItemGroup.ItemTitleState))
async def ItemTitleState_handler(message, state):
	await message.answer(MSGS["seller_add_item__1"])
	await state.update_data(title=message.text)

	await state.set_state(CreateItemGroup.ItemDescState)

@main_router.message(StateFilter(CreateItemGroup.ItemDescState))
async def ItemDescState_handler(message, state):
	await message.answer(MSGS["seller_add_item__2"])
	await state.update_data(desc=message.text)

	await state.set_state(CreateItemGroup.ItemImageState)

@main_router.message(StateFilter(CreateItemGroup.ItemImageState))
async def ItemImageState_handler(message, state):
	try:
		await state.update_data(image=message.photo[0].file_id)
		await message.answer(MSGS["seller_add_item__3"])

		await state.set_state(CreateItemGroup.ItemPriceState)
	except:
		await message.answer(MSGS["seller_add_item__image_error"])

@main_router.message(StateFilter(CreateItemGroup.ItemPriceState))
async def ItemPriceState_handler(message, state):
	if message.text.isdigit():
		await message.answer(MSGS["seller_add_item__4"])
		await state.update_data(price=message.text)

		await state.set_state(CreateItemGroup.ItemCashbackState)
	else:
		await message.answer(MSGS["seller_add_item__price_error"])

@main_router.message(StateFilter(CreateItemGroup.ItemCashbackState))
async def ItemCashbackState_handler(message, state):
	if message.text.endswith("%") and message.text.strip("%").isdigit():
		await message.answer(MSGS["seller_add_item__5"])
		await state.update_data(cashback=message.text.strip("%"))

		await state.set_state(CreateItemGroup.ItemConditionState)
	else:
		await message.answer(MSGS["seller_add_item__cashback_error"])

@main_router.message(StateFilter(CreateItemGroup.ItemConditionState))
async def ItemConditionState_handler(message, state):
	await message.answer(
		MSGS["seller_add_item__6"],
		reply_markup=getCategoriesMarkup())
	await state.update_data(cond=message.text)

	await state.set_state(CreateItemGroup.ItemCategoryState)

@main_router.callback_query(StateFilter(CreateItemGroup.ItemCategoryState))
async def ItemCategoryState_handler(call, state):
	await call.answer()
	await state.update_data(
		category=call.data.replace("category_", "")
	)

	data = (await state.get_data())

	title = data.get("title")
	description = data.get("desc")
	price = data.get("price")
	image = data.get("image")
	cashback = data.get("cashback")
	category = get_category_by_id(data.get("category")).title

	text = MSGS["item_card"].format(
			title,
			description,
			price,
			cashback,
			category
		)

	await bot.send_photo(chat_id=call.from_user.id,
						caption=text,
						photo=image)
	
	await call.message.answer(
		MSGS["seller_add_item__7"],
		reply_markup=getConfirmMarkup())

	await state.set_state(CreateItemGroup.ItemConfirmState)

@main_router.callback_query(StateFilter(CreateItemGroup.ItemConfirmState), F.data == "accept")
async def ItemConfirmState_success_handler(call, state):
	await call.answer()

	data = (await state.get_data())

	title = data.get("title")
	description = data.get("desc")
	price = data.get("price")
	image = data.get("image")
	cashback = data.get("cashback")
	print(data.get("category"))
	category = get_category_by_id(data.get("category")).id

	seller_id = get_seller_id(call.from_user.id)

	create_item(
		title=title,
		desc=data.get("desc"),
		price=price,
		image=image,
		cashback=cashback,
		cond=data.get("cond"),
		seller_id=seller_id,
		cat_id=category)

	users = get_users_with_cat(data.get("category"))
	for user in users:
		try:
			text = MSGS["item_card"].format(
			title,
			description,
			price,
			cashback,
			category)

			await bot.send_photo(
				chat_id=call.from_user.id,
				caption=text,
				photo=image)
		except:
			print("Blocked")

	await call.message.answer(
			MSGS["seller_add_item__success"],
			reply_markup=getSellerMarkup()
			)

	await state.clear()

@main_router.callback_query(StateFilter(CreateItemGroup.ItemConfirmState), F.data == "deny")
async def ItemConfirmState_deny_handler(call, state):
	await call.answer()
	await call.message.answer(
			MSGS["seller_add_item__error"],
			reply_markup=getSellerMarkup()
			)
	
	await state.clear()

@main_router.message(StateFilter(None), F.text == BUTTONS["seller"]["menu"][1])
async def get_seller_items_handler(message, state, user_id=None):
	if user_id == None:
		user_id = message.from_user.id
	items = get_seller_items(user_id)

	if len(items) == 0:
		await message.answer(
			MSGS["seller_no_items"],
			reply_markup=getSellerMarkup())
	else:
		await message.answer(
			MSGS["seller_items"].format(len(items)),
			reply_markup=getSellerItemsMarkup(items)
			)

@main_router.callback_query(StateFilter(None), F.data.startswith("item_"))
async def seller_items_handler(call, state):
	await call.message.delete()

	item = get_item_by_id(call.data.strip("item_"))
	text = MSGS["item_card"].format(
			item.title,
			item.description,
			item.price,
			item.cashback,
			item.category.title
		)

	await bot.send_photo(chat_id=call.from_user.id,
						caption=text,
						photo=item.image,
						reply_markup=getDeleteItemMarkup(item))

@main_router.callback_query(StateFilter(None), F.data.startswith("remove_item__"))
async def remove_item_handler(call, state):
	data = call.data.strip("remove_item__")
	item_id, title = data.split("|")

	delete_item(item_id)

	await call.message.answer(
		MSGS["seller_remove_item_success"].format(
			title))
	await call.message.delete()

	await asyncio.sleep(2)
	await get_seller_items_handler(call.message, state, user_id=call.from_user.id)

@main_router.callback_query(StateFilter(None), F.data == "back")
async def remove_item_handler(call, state):
	await call.answer()
	await get_seller_items_handler(call.message, state, user_id=call.from_user.id)

	await call.message.delete()