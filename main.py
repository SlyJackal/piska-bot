from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=getenv('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет!')


@dp.message_handler()
async def word_in_text(message: types.Message):
    text = message.text.split()
    if {'Вера', 'вера', 'Писька', 'писька'} & set(text):
        await message.answer('Писька!')


if __name__ == '__main__':
    load_dotenv()
    executor.start_polling(dp)
    
    await bot.send_message(84381379, 'text')