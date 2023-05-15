from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
# @dp.message_handler(commands='start')
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС: \nhttps://t.me/pizza_ShotaUAshotaBot')

# @dp.message_handler(commands='help')
async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, 'Создано для обучения в качестве проекта.')
    await message.delete()

# @dp.message_handler(commands='Режим_работы')
async def command_worktime(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 8:00 до 22:00, Пт-Сб с 9:00 до 23:00')

# @dp.message_handler(commands='Расположение')
async def command_adress(message : types.Message):
    await bot.send_message(message.from_user.id, 'Г. Казань, ул. Пушкина, д. 32')

def register_hadlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_worktime, commands=['Режим_работы'])
    dp.register_message_handler(command_adress, commands=['Расположение'])
