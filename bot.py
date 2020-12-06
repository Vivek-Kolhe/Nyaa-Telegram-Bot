from logging import INFO
from pyrogram import Client, filters
import requests
import logging
from autologging import logged, traced
from credentials import *

# Enable logging
logging.basicConfig(
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO)
logger = logging.getLogger(__name__)

app = Client("my_bot", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)
with app:
    botname = app.get_me().username

#####################################################################################################################
# Common function for making request to the API
#####################################################################################################################

def get_data(query, client, message):
    if len(query) == 1:
        text = "No search query found!\nSend /help for help."
        app.send_message(chat_id = message.chat.id, text = text, parse_mode = "html")
    else:
        if query[0][1:] == "eng":
            url = f"https://nyaaapi.herokuapp.com/anime/search?query={query[-1]}&category=eng"
        elif query[0][1:] == "non_eng":
            url = f"https://nyaaapi.herokuapp.com/anime/search?query={query[-1]}&category=non-eng"
        elif query[0][1:] == "raw":
            url = f"https://nyaaapi.herokuapp.com/anime/search?query={query[-1]}&category=raw"
        elif query[0][1:] == "manga":
            url = f"https://nyaaapi.herokuapp.com/manga/search?query={query[-1]}&category=eng"
        
        old_msg = app.send_message(chat_id = message.chat.id, text = "<b>Searching...</b>", parse_mode = "html")
        response = requests.get(url).json()
        if int(response["count"]) < 1:
            text = "No results found!"
            app.edit_message_text(chat_id = message.chat.id, message_id = old_msg.message_id, text = text, parse_mode = "html")
        else:
            data = response["data"]
            text = ""
            for i in range(20):
                try:
                    title = data[i]["title"]
                    seeders = data[i]["seeders"]
                    leechers = data[i]["leechers"]
                    size = data[i]["size"]
                    unique_id = data[i]["id"]

                    text = text + f"<b>{title}</b>\n<b>ID: </b><code>{unique_id}</code>\n<b>Seeders/Leechers: </b>{seeders}/{leechers}\n<b>Size: </b>{size}\n\n"
                    app.edit_message_text(chat_id = message.chat.id, message_id = old_msg.message_id, text = text, parse_mode = "html")
                except:
                    break
            text = "Send **/magnet <unique_id>** from the above list to get the torrent info and magnet link."
            app.send_message(chat_id = message.chat.id, text = text, parse_mode = "markdown")
#####################################################################################################################

# start command
@traced
@logged
@app.on_message(filters.command(["start", f"start@{botname}"], prefixes = "/") & ~filters.edited)
def start(client, message):
    text = f"Hello **{str(message.from_user.first_name)}**!\nI can fetch anime torrents from [Nyaa](nyaa.si).\nSend /help for more info."
    app.send_message(chat_id = message.chat.id, text = text, parse_mode = "markdown")

# help command
@traced
@logged
@app.on_message(filters.command(["help", f"help@{botname}"], prefixes = "/") & ~filters.edited)
def help(client, message):
    text = "**Note:** The bot will fetch some of the most recent torrents, so be specific with search query.\n**Available Commands:**\n/eng, /non_eng and /raw followed by anime name.\n/manga followed by manga name.\n/magnet followed by unique id to get torrent info and torrent.\n\nExamples:\n**/eng Attack on Titan**\n**/non_eng Attack on Titan**\n**/raw Attack on Titan**\n**/manga Attack on Titan**\n**/magnet 1234567**"
    app.send_message(chat_id = message.chat.id, text = text, parse_mode = "markdown")

# command for fetching english anime torrents
@traced
@logged
@app.on_message(filters.command(["eng", f"eng@{botname}"], prefixes = "/") & ~filters.edited)
def eng(client, message):
    query = message.text.split(maxsplit = 1)
    get_data(query, client, message)

# commands for fetching non-english anime torrents
@traced
@logged
@app.on_message(filters.command(["non_eng", f"non_eng@{botname}"], prefixes = "/") & ~filters.edited)
def non_eng(client, message):
    query = message.text.split(maxsplit = 1)
    get_data(query, client, message)

# command for fetching raw anime torrents
@traced
@logged
@app.on_message(filters.command(["raw", f"raw@{botname}"], prefixes = "/") & ~filters.edited)
def raw(client, message):
    query = message.text.split(maxsplit = 1)
    get_data(query, client, message)

# command for manga search
@traced
@logged
@app.on_message(filters.command(["manga", f"manga@{botname}"], prefixes = "/") & ~filters.edited)
def manga(client, message):
    query = message.text.split(maxsplit = 1)
    get_data(query, client, message)

# command for magnet link and torrent info
@traced
@logged
@app.on_message(filters.command(["magnet", f"magnet@{botname}"], prefixes = "/") & ~filters.edited)
def torrent(client, message):
    query = message.text.split(maxsplit = 1)
    if len(query) == 1:
        text = "No unique id found!\nSend /help for help."
        app.send_message(chat_id = message.chat.id, text = text, parse_mode = "html")
    else:
        query = query[-1]
        response = requests.get(f"https://nyaaapi.herokuapp.com/anime/search?id={query}").json()
        try:
            title = response["info"]["title"]
            seeders = response["info"]["seeders"]
            leechers = response["info"]["leechers"]
            size = response["info"]["size"]
            uploader = response["info"]["uploader"]
            torrent = response["info"]["torrent"]
            magnet = response["info"]["magnet"]

            text = f"<b>{title}</b>\n<b>Seeders/Leechers:</b> <code>{seeders}/{leechers}</code>\n<b>Size:</b> <code>{size}</code>\n<b>Uploader:</b> <code>{uploader}</code>\n<b>Torrent:</b> <a href='{torrent}'>Click here!</a>\n<b>Magnet:</b> <code>{magnet}</code>\n"

        except:
            text = response["info"]["error"]

        app.send_message(chat_id = message.chat.id, text = text, parse_mode = "html")
app.run()
