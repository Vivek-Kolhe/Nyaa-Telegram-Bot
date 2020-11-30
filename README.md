# Nyaa-Telegram-Bot
A telegram bot made in python to fetch anime torrents from Nyaa.si. The bot uses [Nyaa-API](https://github.com/Vivek-Kolhe/Nyaa-API) made by me.

## Dependencies
- Requests\
  ```pip3 install requests```

- Pyrogram\
  ```pip3 install pyrogram```

- Autologging\
  ```pip3 install Autologging```

***Or Use:***\
  ```pip3 install -r requirements.txt```

## Available Commands
| **Commands** | **Description** |
|---|---|
| ```/start``` | Starts the bot. |
| ```/help``` | Help regarding the bot. |
| ```/eng <query>``` | Searches for English translated anime. |
| ```/non_eng <query>``` | Searches for Non-English anime. |
| ```/raw <query>``` | Searches for raw anime. |
| ```/magnet <unique_id>``` | Returns magnet link and torrent info. |

## Set-Up
Clone and download the repository. Install all the above listed dependencies and run ***bot.py*** using ```python3 bot.py```.

## Deploying on Heroku
- Clone and download the repository.
- Get your telegram **api_id** and **api_hash** from https://my.telegram.org/ and pass them on line 12 and 13.
- Get **bot_token** from [BotFather](https://t.me/BotFather) and pass it on the line 14.
- Download **HerokuCLI** and create an from the dashboard.
- Navigate inside the directory where all the repo files are present and run the following commands.
    ```
    heroku login
    heroku git:remote -a appname
    git init
    git add .
    git commit -am "deploying"
    git push heroku master
    ```
***Note:*** Pass the **api_id** as an integer.

I know I've repeated my code atleast 2-3 times, I'll fix it later. Or you guys can contribute as well :).
Thanks [Infinity-Plus](https://github.com/infinity-plus) for his help.
