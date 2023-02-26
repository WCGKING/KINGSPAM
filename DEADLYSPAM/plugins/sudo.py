
# Copyright © 2023-2024 by piroxpower@Github, < https://github.com/piroxpower >.
#
# This file is part of < https://github.com/Team-Deadly/DEADLYSPAM > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Deadly/DEADLYSPAM/blob/main/LICENSE >
#
# All rights reserved ®.



import os
import asyncio
import sys
import git
import config
# Changed root to DEADLYSPAM
from DEADLYSPAM import BOT0, SUDOERS, CHUT
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, version

hl = config.CMD_HNDLR 

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id in CHUT:
       if event.reply_to_msg_id is not None:
           reply_msg = await event.get_reply_message()
           user_id = reply_msg.sender_id
           ok = await event.reply("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 🥀**")
           if user_id in SUDOERS:
               await ok.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ  ɪɴ   ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
           else:
               SUDOERS.append(user_id) 
               await ok.edit(f"ᴀᴅᴅᴇᴅ {user_id} ᴛᴏ ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
       else:
           await event.reply(f"**» ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ! **")



@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdelsudo(?: |$)(.*)" % hl))
async def delb(event):
    if event.sender_id in CHUT:
         if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            ok = await event.reply("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 🥀**")
            if user_id not in SUDOERS:
                await ok.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ  ɪɴ   ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
            else:
                SUDOERS.remove(user_id) 
                await ok.edit(f"ʀᴇᴍᴏᴠᴇᴅ {user_id} ғʀᴏᴍ ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
         else:
             await event.reply(f"**» ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ! **")
