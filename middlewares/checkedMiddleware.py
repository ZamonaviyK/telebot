import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from keyboards.inline.subcribInline import subsButton
from utils.misc import subscription
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            if update.message.text == '/start':
                return
            user = update.message.from_user.id
        elif update.callback_query:
            if update.callback_query.data == "check_subs":
                return
            user = update.callback_query.from_user.id
        else:
            return
        logging.info(user)
        result = f"Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling!\n"
        final_status = True
        f = open('data/chanels/chanel.txt', 'r')
        read = f.read()
        f.close()
        read = read.split('\n')
        read.pop()
        arr = []
        for channel in read:
            status = await subscription.check(user_id=user, channel=channel)
            if not status:
                chanel = await bot.get_chat(channel)
                arr.append(await chanel.export_invite_link())
        if len(arr) < 1:
            return
        subBtn = await subsButton(values=arr)
        await update.message.answer("Siz quyidagi kanallarga obuna boling!",reply_markup=subBtn)
            # for channel in CHANNELS:
        #     status = await subscription.check(user_id=user, channel=channel)
        #     final_status *= status
        #     channel = await bot.get_chat(channel)
        #     if not status:
        #         invite_link = await channel.export_invite_link()
        #
        #         result += f"👉🏽 <b><a href='{invite_link}'>{channel.title}</a></b>\n\n"
        #     if not final_status:
        #         await update.message.answer(result, disable_web_page_preview=True)
        #         raise CancelHandler()
