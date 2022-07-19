import os
import re

from keyboards.inline.subcribInline import subsButton
from loader import bot
from aiogram.dispatcher import filters, FSMContext
from aiogram import types
from loader import dp
from utils.misc import subscription
import requests

REGEX = f""
BASE_URL = 'https://fakestoreapi.com'


@dp.message_handler(commands='list')
async def list_users(message: types.Message):
    list = requests.get(BASE_URL)
    text = ''
    for user in list:
        text += f'Id: {user.tele_id}\nFullName: {user.name}\nUserName {user.username}\n\n'
