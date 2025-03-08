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
	print("Hello, friend!")

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

	logging.basicConfig(
		level=logging.INFO,
		stream=sys.stdout
		)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		shutdown()