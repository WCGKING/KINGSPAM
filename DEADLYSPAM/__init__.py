import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#VERSION
deadlyversion = "v3.0.0"

#SUDOERS
HEHE = "5937170640"
SUDOERS = int(HEHE) 
OWNER = config.OWNER_ID
SUDOERS.append(int(OWNER))

# ECHO LIST
LUND = "123456789"
ECHOUSER = int(LUND) 
# CLIENTS

BOT0 = TelegramClient('BOT0', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

BOT1 = TelegramClient('BOT1', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
