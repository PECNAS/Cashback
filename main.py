import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from token_config import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(
		token=TOKEN,
		default=DefaultBotProperties(
			parse_mode=ParseMode.HTML
			)
		)

def startup():
	cats = get_categories()
	if cats == []:
		create_category("Техника")
		create_category("Дом")
		create_category("Хобби")
		create_category("Инструменты")
		create_category("Освещение")
		create_category("Одежда")
		create_category("Аксессуары")
		create_category("Цветы")

	clients, sellers, moders, cats, items, reqs = get_startup_info()
	print(f"\n\nBot is started!\n\
Number of clients: {clients}\n\
Number of sellers: {sellers}\n\
Number of moderators: {moders}\n\
Number of categories: {cats}\n\
Number of items: {items}\n\
Number of requests: {reqs}\n\n")

def shutdown():
	print("Goodbye, friend!")

async def main() -> None:
	startup()
	await dp.start_polling(bot)

if __name__ == "__main__":
	from imports import *

	from handlers.commands_handler import *
	from handlers.client_handler import *
	from handlers.seller_handler import *
	from handlers.admin_handler import *
	from handlers.moderator_handler import *

	logging.basicConfig(
		level=logging.INFO,
		stream=sys.stdout
		)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		shutdown()