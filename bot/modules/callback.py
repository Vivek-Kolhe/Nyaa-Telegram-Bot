from bot import NYAA
from .get_response import nyaa, nyaa_id, sukebei, sukebei_id
from pyrogram import filters
from pyrogram.types import CallbackQuery

@NYAA.on_callback_query()
async def _callback(client, CallbackQuery):
    query = CallbackQuery.data.split(maxsplit = 2)
    if len(query) == 3:
        if query[0] in ["anime", "manga", "audio", "live_action", "software", "pictures"]:
            data = await nyaa(query)
        elif query[0] in ["art", "real"]:
            data = await sukebei(query)
        
        if len(data) < 1:
            await CallbackQuery.edit_message_text(text = "No results found!")
        else:
            text = ""
            for i in range(20):
                try:
                    title = data[i]["title"]
                    seeders = data[i]["seeders"]
                    leechers = data[i]["leechers"]
                    size = data[i]["size"]
                    unique_id = data[i]["id"]

                    text = text + f"<b>{title}</b>\n<b>ID: </b><code>{unique_id}</code>\n<b>Seeders/Leechers: </b>{seeders}/{leechers}\n<b>Size: </b>{size}\n\n"
                    await CallbackQuery.edit_message_text(text = text)
                except Exception:
                    break
            text = "Send **/magnet <unique_id>** from the above list to get the torrent info and magnet link."
            await NYAA.send_message(chat_id = CallbackQuery.from_user.id, text = text)
    elif len(query) == 2:
        if query[0] == "nyaa":
            data = await nyaa_id(query[-1])
        elif query[0] == "sukebei":
            data = await sukebei_id(query[-1])
        try:
            title = data["title"]
            seeders = data["seeders"]
            leechers = data["leechers"]
            size = data["size"]
            uploader = data["uploader"]
            torrent = data["torrent"]
            magnet = data["magnet"]

            text = f"<b>{title}</b>\n<b>Seeders/Leechers:</b> <code>{seeders}/{leechers}</code>\n<b>Size:</b> <code>{size}</code>\n<b>Uploader:</b> <code>{uploader}</code>\n<b>Torrent:</b> <a href='{torrent}'>Click here!</a>\n<b>Magnet:</b> <code>{magnet}</code>\n"
        
        except Exception as e:
            text = f"Error:\n{e}"
        
        await CallbackQuery.edit_message_text(text = text, parse_mode = "html")