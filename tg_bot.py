import asyncio
from aiogram import Bot, Dispatcher


TOKEN = open('token.txt').read()
CHANNEL_ID = "-1002336458413"


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def send_message(res):
    message = f"{res}"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    print("Сообщение отправлено")
    await asyncio.sleep(2)

    