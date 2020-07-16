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
    if {'Вера', 'вера', 'Писька', 'писька', 'Писька!', 'писька!', 'Веры', 'веры'} & set(text):
        await message.answer('Писька!')
    if {'Вова'} & set(text):
        await message.answer('Я не буду писать это слово!')
    if {'Никита'} & set(text):
        await message.answer('Котлетка!')
    if {'Игорь', 'Иииииигооорь Котов'} & set(text):
        await message.answer('Жрать!')
    if {'Наташа'} & set(text):
        await message.answer('Бежать!')
    if {'Алексей'} & set(text):
        await message.answer('Папка!')


if __name__ == '__main__':
    load_dotenv()
    executor.start_polling(dp)
