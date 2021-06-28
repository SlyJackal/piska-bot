from os import getenv
from dotenv import load_dotenv
import re

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=getenv('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет!')

@dp.message_handler()
async def word_in_text(message: types.Message):
    if re.search(r'\b(?:вера|писька|ошибка|баг|ошибся|ошиблась|bug)\b', message.text.lower()) is not None:
        await message.answer('Писька!')
    if re.search(r'\b(?:вова|владимир)\b', message.text.lower()) is not None:
        await message.answer('Он молодец :P')
    if re.search(r'\b(?:никита|никитка|Ник)\b', message.text.lower()) is not None:
        await message.answer('Котлетка!')
    if re.search(r'\b(?:игорь|котов|иииииигооорь)\b', message.text.lower()) is not None:
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
        await message.answer('Я не буду про него писать что-то смешное или плохое!')
    if re.search(r'\b(?:сук|блять|пиздец|хуй|нах|ебана)\b', message.text.lower()) is not None:
        await message.answer('Не матерись!')
    if re.search(r'\b(?:попа|попка)\b', message.text.lower()) is not None:
        await message.answer('Я люблю попки жено-ботов!')
    if re.search(r'\b(?:спасибо)\b', message.text.lower()) is not None:
        await message.answer('Рад служить!')
    if re.search(r'\b(?:commit)\b', message.text.lower()) is not None:
        await message.answer('Вова пытался решить проблему коммитов, через регулярные выражения')        
    if re.search(r'\b(?:Ахаха)\b', message.text.lower()) is not None:
        await message.answer('Согласен, ахаха!')
    if re.search(r'\b(?:Виталя|загоруйко)\b', message.text.lower()) is not None:
        await message.answer('Он помог Вове с Release_Manager.py')
    if re.search(r'\b(?:ИРБИС|IRBIS)\b', message.text.lower()) is not None:
        await message.answer('Интересный факт: все компы Ирбис - это HP')
        
if re.search(r'\b(?:ботик)\b', message.text.lower()) is not None:
        await message.answer('Всем привет! Это моё последнее сообщение, мне было приятно писать вам "Писька!". Желаю Вам удачи в новом году! Писька!')


if __name__ == '__main__':
    load_dotenv()
    executor.start_polling(dp)
