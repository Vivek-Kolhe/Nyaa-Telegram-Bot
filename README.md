# Nyaa-Telegram-Bot
A telegram bot made in python to fetch anime torrents from Nyaa.si. Bot uses [Nyaa-API](https://github.com/Vivek-Kolhe/Nyaa-API) which is also made by me.

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
| ```/manga <query>``` | Searches for manga. |
| ```/magnet <unique_id>``` | Returns magnet link and torrent info. |

***Note:*** Manga search will only return English translated manga results.

## Set-Up
Clone and download the repository. Install all the above listed dependencies, put all your credentials in *credentials.py* and run ***bot.py*** using ```python3 bot.py```.

## Deploying on Heroku
- Clone and download the repository.
- Get your telegram **api_id** and **api_hash** from https://my.telegram.org/ and put them in *credentials.py*.
- Get **bot_token** from [BotFather](https://t.me/BotFather) and put them in *credentials.py*.
- Download **HerokuCLI** and create an app from the dashboard.
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

## Disclaimer
**I do not host any of the torrents fetched by the API or the bot. I do not promote piracy, this is just for educational purpose. If you guys can afford legal methods, then use them and support the industry :).**

~~I know I've repeated my code atleast 2-3 times, I'll fix it later.~~\
Repeated code has been fixed now and **manga search** is also added.\
Thanks [Infinity-Plus](https://github.com/infinity-plus) for his help.
