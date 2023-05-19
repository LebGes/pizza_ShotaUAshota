from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Бот в онлайне')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_hadlers_client(dp)
admin.register_handler_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)