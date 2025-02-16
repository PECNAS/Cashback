from imports import *

@main_router.message(StateFilter(None), F.text == BUTTONS["user"]["start"][0])
async def buyer_handler(message, state):
	pass