from telethon import TelegramClient
from decouple import config
import logging
import time
from os import getenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

UstaD = TelegramClient('UstaD', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

UstaD2 = TelegramClient('UstaD2', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

UstaD3 = TelegramClient('UstaD3', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

UstaD4 = TelegramClient('UstaD4', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

UstaD5 = TelegramClient('UstaD5', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

UstaD6 = TelegramClient('UstaD6', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

UstaD7 = TelegramClient('UstaD7', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

UstaD8 = TelegramClient('UstaD8', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

UstaD9 = TelegramClient('UstaD9', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

UstaD10 = TelegramClient('UstaD10', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10) 
