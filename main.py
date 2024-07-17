import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from datetime import datetime

API_TOKEN = "6892378455:AAFB0lo4ESrliOoMT5h3kXYLOVFk009YeCw"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hellow, {message.from_user.full_name}")

@dp.message()
async def add_note(message: Message) -> None:
    with open('new_note.md', 'a') as file:
        file.write(f"##Новая заметка от {datetime.now()}\n {message.text}\n")

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
