from aiogram import types
from loader import dp
from utils.misc import subscription
import requests

REGEX = f""
BASE_URL = 'http://127.0.0.1:8000/list/'


@dp.message_handler(commands='list')
async def list_users(message: types.Message):
    list = requests.get(BASE_URL).json()
    text = ''
    print(list)
    for user in list:
        text+=f"USER_ID: {user['tele_id']}\nName: {user['name']}\n username:{user['username']}\n\n"
    await message.answer(text)
