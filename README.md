# Nyaa-Telegram-Bot
A telegram bot made in python to fetch torrents from [Nyaa](https://nyaa.si/) and [Sukebei](https://sukebei.nyaa.si/). Bot uses [Nyaa-API](https://github.com/Vivek-Kolhe/Nyaa-API) which is also made by me.

## Dependencies
- Aiohttp\
  ```pip3 install aiohttp```

- Pyrogram\
  ```pip3 install pyrogram```

***Or Use:***\
  ```pip3 install -r requirements.txt```

## Set-Up
Clone and download the repository. Install all the above listed dependencies, put all your credentials in *config.py* and run the bot using ```python3 -m bot```.

## Deploying on Heroku
- Clone and download the repository.
- Get your telegram **api_id** and **api_hash** from [here](https://my.telegram.org/) and put them in *config.py*.
- Get **bot_token** from [BotFather](https://t.me/BotFather) and put it in *config.py*.
- Download **HerokuCLI** and create an app from the dashboard.
- Navigate inside the directory where all the repo files are present and run the following commands.
    ```
    heroku login
    heroku git:remote -a <appname>
    git init
    git add .
    git commit -am "deploying"
    git push heroku master
    ```
***Note:*** Pass the **api_id** as an integer.

## Disclaimer
**I do not host any of the torrents fetched by the API or the bot. I do not promote piracy, this is just for educational purpose. If you guys can afford legal methods, then use them and support the industry :).**

~~I know I've repeated my code atleast 2-3 times, I'll fix it later.~~\
~~Repeated code has been fixed now and **manga search** is also added.~~\
Now supports each and every single category and sub category of torrents from Nyaa and Sukebei.\
Thanks [Infinity-Plus](https://github.com/infinity-plus) for his help.
