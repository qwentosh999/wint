import asyncio
from app.handlers.start_router import start_router 


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(botstastastsaxashdgshjag)


if __name__ == "__main__":
    asyncio.run(main())