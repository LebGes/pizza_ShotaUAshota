from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот в онлайне')

'''*****************************************КЛИЕНТСКАЯ ЧАСТЬ*********************************************************'''
@dp.message_handler(commands='start')
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать')
        await message.delete()
    except:
        await message.reply('Пиши боту: \nhttps://t.me/pizza_ShotaUAshotaBot')

@dp.message_handler(commands='help')
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Создано для обучения в качестве проекта.\n Abdurakhmanov Anvar 2023')
    await message.delete()
'''*****************************************АДМИНСКАЯ ЧАСТЬ*********************************************************'''

'''*****************************************ОБЩАЯ ЧАСТЬ*********************************************************'''


executor.start_polling(dp, skip_updates=True)