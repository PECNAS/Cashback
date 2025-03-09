from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["moder"]["menu"]["check"])
async def check_handler(message, state):
	reqs = get_requests()
	if len(reqs) == 0:
		await message.answer(MSGS["moder_no_reqs"])
		return

	request = reqs[0]
	item = get_item_by_id(request.item_id)
	client = check_user(request.client_id).get("object")

	await message.answer(
		MSGS["moder_request"].format(
			item.title,
			item.id,
			item.link,
			item.cashback_condition,
			client.tg_id,
			client.username),
		reply_markup=getCloseRequestMarkup(request.id))

@main_router.callback_query(StateFilter(None), F.data.startswith("close__"))
async def close_req_handler(call, state):
	req_id = call.data.strip("close__")
	close_request(req_id)
	await call.message.answer(MSGS["moder_request_closed_success"])
	await call.message.delete()