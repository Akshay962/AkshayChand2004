# sahid malik
import asyncio
import requests
from requests import get
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp


@Client.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await message.reply_sticker(
        sticker=("CAACAgUAAxkBAAIQymL-dsDh9QXCqpAQ6N7qoyvONyTJAALhBgACIomwVFm0oA-q0Sh9HgQ"),
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        await message.reply_photo(
            photo=req,
            caption=(MALIK.format(message.from_user.mention, temp.U_NAME, temp.B_NAME, message.chat.title, req)),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("๐น ๐๐๐ก๐๐๐ง๐๐ฅ๐ ๐น", url=f"{req}")]]
            ),
        )
        await asyncio.sleep(0.3)
        await m.delete()

MALIK = """Successfully Written Text ๐\n\n๐ฅธRequested by :{}.\n๐นWritten By <a href=https://t.me/{}>{}</a>,\n๐ป Group: {}.\n๐Link :{}"""

MALIKK = """Hey {}.\n\nPlease wait...,\n\nWriting your text.."""



