from os import getenv
from dotenv import load_dotenv
import re

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=getenv('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет!')


#@dp.message_handler()
#async def word_in_text(message: types.Message):
 #   text = message.text.split()
  #  if {'Вера', 'вера', 'Писька', 'писька', 'Писька!', 'писька!', 'Веры', 'веры', 'Вера?'} & set(text):
   #     await message.answer('Писька!')
    #if {'Вова', 'Вова?', 'Вова!'} & set(text):
     #   await message.answer('Я не буду писать это слово!')
    #if {'Никита', 'Никита?', 'Никита!'} & set(text):
        #await message.answer('Котлетка!')
    #if {'Игорь', 'Игорь?', 'Игорь!'} & set(text):
    #    await message.answer('Жрать!')
    #if {'Наташа', 'Наташа?', 'Наташа!'} & set(text):
    #    await message.answer('Бежать!')
    #if {'Алексей', 'Алексей?', 'Алексей!'} & set(text):
    #    await message.answer('Папка!')
    #if {'регресс'} & set(text):
    #    await message.answer('ПИСЬКА! ПИСЬКА! ПИСЬКА!')

@dp.message_handler()
async def word_in_text(message: types.Message):
    if re.search(r'\b(?:вера|писька)\b', message.text.lower()) is not None:
        await message.answer('Писька!')

if __name__ == '__main__':
    load_dotenv()
    executor.start_polling(dp)
