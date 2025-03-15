from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.keybroads.all_kb import main_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по' + \
        'команде /start используя фильтр CommandStart()',
        reply_markup=main_kb(message.from_user.id))