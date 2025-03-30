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
	await state.update_data(cat=category)
	await call.message.answer(
		MSGS["min_cashback"])
	await call.message.delete()

	await state.set_state(ClientGroup.MinCashbackState)

@main_router.message(StateFilter(ClientGroup.MinCashbackState))
async def MinCashbackState_handler(message, state):
	if message.text.endswith("%") and message.text.strip("%").isdigit():
		category = (await state.get_data()).get("cat")
		create_client(
			message.from_user.id,
			message.from_user.username,
			category,
			message.text.strip("%"))
		await message.answer(
			MSGS["client_created_success"],
			reply_markup=getClientMarkup())
		await state.clear()
	else:
		await message.answer(MSGS["seller_add_item__cashback_error"])

@main_router.message(StateFilter(None), F.text == BUTTONS["client"]["menu"]["show_items"])
async def show_items_handler(message, state):
	await message.answer(
		MSGS["client_show_items"],
		reply_markup=getCategoriesMarkup())
	await state.set_state(ShowItemsGroup.CategoryState)

@main_router.callback_query(StateFilter(ShowItemsGroup.CategoryState))
async def CategoryState_catalog_handler(call, state, query=None, message=None):
	if not query:
		await call.answer()
		
		cat_id = call.data.strip("category_")
		items = get_items_in_category(cat_id)
		await state.update_data(current_category=cat_id)

		if not items:
			await call.message.answer(
				MSGS["client_no_items"],
				reply_markup=getClientMarkup())
			await state.set_state(None)
			return

		chat_id = call.from_user.id
		await call.message.delete()

	if query:
		items = get_items_by_query(query)
		if not items:
			await message.answer(
				MSGS["client_no_items"],
				reply_markup=getClientMarkup())
			await state.set_state(None)
			return

		chat_id = message.from_user.id

	await state.set_state(ShowItemsGroup.ItemsListState)

	await state.update_data(items=items)
	await state.update_data(current_item=0)

	item = items[0]
	text = MSGS["item_card"].format(
			item.title,
			item.description,
			item.price,
			item.cashback,
			item.category.title,
			item.cashback_condition)

	await bot.send_photo(
		chat_id=chat_id,
		caption=text,
		photo=item.image,
		reply_markup=getClientMenuMarkup(link=item.link))

@main_router.callback_query(StateFilter(ShowItemsGroup.ItemsListState), F.data == "back")
async def ItemsListState_back_handler(call, state):
	data = (await state.get_data())
	items = data.get("items")
	current_item = data.get("current_item")

	if current_item == 0:
		current_item = len(items) - 1
	else:
		current_item -= 1

	await state.update_data(current_item=current_item)

	item = items[current_item]
	text = MSGS["item_card"].format(
			item.title,
			item.description,
			item.price,
			item.cashback,
			item.category.title,
			item.cashback_condition)

	await bot.send_photo(
		chat_id=call.from_user.id,
		caption=text,
		photo=item.image,
		reply_markup=getClientMenuMarkup(link=item.link))

	await call.message.delete()

@main_router.callback_query(StateFilter(ShowItemsGroup.ItemsListState), F.data == "next")
async def ItemsListState_next_handler(call, state):
	data = (await state.get_data())
	items = data.get("items")
	current_item = data.get("current_item")


	if current_item == len(items) - 1:
		current_item = 0
	else:
		current_item += 1

	await state.update_data(current_item=current_item)

	item = items[current_item]
	text = MSGS["item_card"].format(
			item.title,
			item.description,
			item.price,
			item.cashback,
			item.category.title,
			item.cashback_condition)

	await bot.send_photo(
		chat_id=call.from_user.id,
		caption=text,
		photo=item.image,
		reply_markup=getClientMenuMarkup(link=item.link))

	await call.message.delete()


@main_router.callback_query(StateFilter(ShowItemsGroup.ItemsListState), F.data == "close")
async def ItemsListState_close_handler(call, state):
	await state.clear()
	await call.message.answer(
		MSGS["client_close_items_list"],
		reply_markup=getClientMarkup())

	await call.message.delete()

@main_router.callback_query(StateFilter(ShowItemsGroup.ItemsListState), F.data == "check")
async def ItemsListState_check_handler(call, state):
	client_id = call.from_user.id

	data = (await state.get_data())
	items = data.get("items")
	item_id = items[data.get("current_item")].id

	if not get_current_request(client_id, item_id):
		create_request(client_id, item_id)

		await call.answer()
		await call.message.answer(
			MSGS["client_request_created"])
	else:
		await call.message.answer(
			MSGS["client_request_error"])

@main_router.callback_query(F.data.startswith("check_new"))
async def check_new_handler(call, state):
	item_id = call.data.strip("check_new__")

	if not get_current_request(call.from_user.id, item_id):
		create_request(call.from_user.id, item_id)
		await call.answer()
		await call.message.answer(
			MSGS["client_request_created"])
	else:
		await call.message.answer(
			MSGS["client_request_error"])

@main_router.message(StateFilter(None), F.text == BUTTONS["client"]["menu"]["find_items"])
async def find_items_handler(message, state):
	await message.answer(MSGS["client_find_items__start"])
	await state.set_state(ClientGroup.FindItemsState)

@main_router.message(StateFilter(ClientGroup.FindItemsState))
async def FindItemsState_handler(message, state):
	await CategoryState_catalog_handler(None, state, message.text, message)