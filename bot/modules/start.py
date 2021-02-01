from bot import NYAA, botname
from pyrogram import Client, filters

START_TEXT = """
Hello!
I can fetch torrents from [Nyaa](https://nyaa.si) and [Sukebei](https://sukebei.nyaa.si).
Send /help for more info.
"""

@NYAA.on_message(filters.command(["start", f"start@{botname}"], prefixes = "/") & ~filters.edited)
async def start(client, message):
    await NYAA.send_message(chat_id = message.chat.id, text = START_TEXT, disable_web_page_preview = True)