import asyncio
import logging
import os
import setting
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from datetime import datetime

API_TOKEN = setting.API_TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hellow, {message.from_user.full_name}")

@dp.message()
async def add_note(message: Message) -> None:
    with open('/home/obsidian_telegram_bot/new_note.md', 'a') as file:
        file.write(f"##Новая заметка от {datetime.now()}\n {message.text}\n")
    os.system("git add .")
    os.system(f'git commit -m "Добавление быстрой заметки в {datetime.now()}"')
    os.system("git push origin main")

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
