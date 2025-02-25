import asyncio

from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from time import strptime

from main import dp, bot
from config import MSGS, BUTTONS
from keyboards import *
from states import *
from database import *

main_router = Router()
dp.include_router(main_router)