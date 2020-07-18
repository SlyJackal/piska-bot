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
    if re.search(r'\b(?:вова|владимир)\b', message.text.lower()) is not None:
        await message.answer('Он молодец :P')
    if re.search(r'\b(?:никита|никитка|Ник)\b', message.text.lower()) is not None:
        await message.answer('Котлетка!')
    if re.search(r'\b(?:Игорь|Котов|иииииигооорь)\b', message.text.lower()) is not None:
        await message.answer('Жрать!')
    if re.search(r'\b(?:наташа|нат|наташка)\b', message.text.lower()) is not None:
        await message.answer('Бежать!')
    if re.search(r'\b(?:алексей|леша|лёха|лёша|леха)\b', message.text.lower()) is not None:
        await message.answer('Папка!')
    if re.search(r'\b(?:регресс|срочно|надо)\b', message.text.lower()) is not None:
        await message.answer('ПИСЬКА! ПИСЬКА! ПИСЬКА!')
    if re.search(r'\b(?:загоруйка|виталя)\b', message.text.lower()) is not None:
        await message.answer('Всякий!')
    if re.search(r'\b(?:антон|старовойтов)\b', message.text.lower()) is not None:
        await message.answer('Сила!')
    if re.search(r'\b(?:сук|блять|пиздец|хуй|нах)\b', message.text.lower()) is not None:
        await message.answer('Не матерись!')
    if re.search(r'\b(?:попа|попка)\b', message.text.lower()) is not None:
        await message.answer('Я люблю попки жено-ботов!')
    if re.search(r'\b(?:спасибо)\b', message.text.lower()) is not None:
        await message.answer('Рад служить!')

if __name__ == '__main__':
    load_dotenv()
    executor.start_polling(dp)
