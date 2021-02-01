from bot.config import Config
from pyrogram import Client

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

NYAA = Client("Nyaa", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)
with NYAA:
    botname = NYAA.get_me().username
