from bot import NYAA, botname
from .get_response import sukebei
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

TEXT = """
Select torrent category:
"""

INVALID_TEXT = """
No search query found!
"""

@NYAA.on_message(filters.command(["art", f"art@{botname}"], prefixes = "/") & ~filters.edited)
async def get_art(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Anime", f"art anime {query[-1]}"),
                    InlineKeyboardButton("Doujinshi", f"art doujinshi {query[-1]}")
                ],
                [
                    InlineKeyboardButton("Manga", f"art manga {query[-1]}"),
                    InlineKeyboardButton("Games", f"art games {query[-1]}")
                ],
                [
                    InlineKeyboardButton("Pictures", f"art pictures {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["real", f"real@{botname}"], prefixes = "/") & ~filters.edited)
async def get_real(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Photos", f"real photos {query[-1]}"),
                    InlineKeyboardButton("Videos", f"real videos {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))