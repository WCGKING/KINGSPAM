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
from DEADLYSPAM import BOT0, SUDOERS
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, version

hl = config.CMD_HNDLR 
OWNER_ID = config.OWNER_ID

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id in OWNER_ID:
        ok = await event.reply("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 🥀**")
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"**» ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ! **")
        if user.id in SUDOERS:
            await ok.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ  ɪɴ   ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
        else:
            SUDOERS.append(target) 
            await ok.edit(f"ᴀᴅᴅᴇᴅ {target} ᴛᴏ ꜱᴜᴅᴏʟɪꜱᴛ 💫") 



@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdelsudo(?: |$)(.*)" % hl))
async def delb(event):
    if event.sender_id in OWNER_ID:
        ok = await event.reply("**ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 🥀**")
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"**» ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ! **")
        if user.id not in SUDOERS:
            await ok.edit("ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ  ɪɴ   ꜱᴜᴅᴏʟɪꜱᴛ 💫") 
        else:
            SUDOERS.remove(target) 
            await ok.edit(f"ʀᴇᴍᴏᴠᴇᴅ {target} ғʀᴏᴍ ꜱᴜᴅᴏʟɪꜱᴛ 💫") 


        
                  
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
