
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"


Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/Deadly_spambot"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/TheDeadlyBots")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://github.com/Team-Deadly/DEADLY-SPAMBOT")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Blaze](tg://user?id={5256676062})"
        sudo_user = ""
        if e.sender_id in OWNER_ID:
            sudo_user = "True"
        else:
            sudo_user = "False"
        DEADLY_ON = f"""
Hey {mention},
This Is Deadly Spam Bot!

Owner:- {myOwner}
OWNER:- {sudo_user}
Creator:- {creator}

Click Below Button For Detailed informations!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
