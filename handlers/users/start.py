from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from loader import dp, bot

BASE_URL = 'http://127.0.0.1:8000/create/'


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def show_channels(message: types.Message):
    new_user = {
        "tele_id": f'{message.from_user.id}',
        "name": f'{message.from_user.full_name}',
        "username": f'{message.from_user.username}'
    }

    responce = requests.post(f'{BASE_URL}', json=new_user)
    if(responce.status_code==201):
        text = f"Assalomu alaykum, {message.from_user.full_name}\n\nBizning Task botimizga Hush kelibsiz!"
    else:
        text = f"User qo'shishda xatolik yuz berdi"
    await message.answer(text)

