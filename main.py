import asyncio
import sqlite3
from create_bot import bot, dp
from app.handlers.start_router import start_router


async def main():
	dp.include_router(start_router)
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)



if __name__ == "__main__":
	asyncio.run(main())