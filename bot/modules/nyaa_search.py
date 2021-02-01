from bot import NYAA, botname
from .get_response import nyaa
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

TEXT = """
Select torrent category:
"""

INVALID_TEXT = """
No search query found!
"""

@NYAA.on_message(filters.command(["anime", f"anime@{botname}"], prefixes = "/") & ~filters.edited)
async def get_anime(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("AMV", f"anime amv {query[-1]}")
                ],
                [
                    InlineKeyboardButton("Eng", f"anime eng {query[-1]}"),
                    InlineKeyboardButton("Non-Eng", f"anime non-eng {query[-1]}"),
                    InlineKeyboardButton("Raw", f"anime raw {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["manga", f"manga@{botname}"], prefixes = "/") & ~filters.edited)
async def get_manga(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Eng", f"manga eng {query[-1]}"),
                    InlineKeyboardButton("Non-Eng", f"manga non-eng {query[-1]}"),
                    InlineKeyboardButton("Raw", f"manga raw {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["audio", f"audio@{botname}"], prefixes = "/") & ~filters.edited)
async def get_audio(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Lossy", f"audio lossy {query[-1]}"),
                    InlineKeyboardButton("Lossless", f"audio lossless {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["live_action", f"live_action@{botname}"], prefixes = "/") & ~filters.edited)
async def get_live_action(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Promo", f"live_action promo {query[-1]}"),
                    InlineKeyboardButton("Raw", f"live_action raw {query[-1]}")
                ],
                [
                    InlineKeyboardButton("Eng", f"live_action eng {query[-1]}"),
                    InlineKeyboardButton("Non-Eng", f"live_action non-eng {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["pictures", f"pictures@{botname}"], prefixes = "/") & ~filters.edited)
async def get_pictures(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Photos", f"pictures photos {query[-1]}"),
                    InlineKeyboardButton("Graphics", f"pictures graphics {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))

@NYAA.on_message(filters.command(["software", f"software@{botname}"], prefixes = "/") & ~filters.edited)
async def get_software(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) < 2:
        await NYAA.send_message(chat_id = message.chat.id, text = INVALID_TEXT)
        return
    
    buttons = [
                [
                    InlineKeyboardButton("Applications", f"software applications {query[-1]}"),
                    InlineKeyboardButton("Games", f"software games {query[-1]}")
                ]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = TEXT, reply_markup = InlineKeyboardMarkup(buttons))