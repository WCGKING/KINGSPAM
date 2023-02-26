
import asyncio
import base64
import config
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDOERS, ECHOUSER
from resources.data import GROUP, DEADLYSPAM

hl = config.CMD_HNDLR

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : ECHO**\n\nCommand :\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDOERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in DEADLYSPAM:
                    text = "**ᴄᴀɴɴᴏᴛ ᴇᴄʜᴏ ᴏɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ !**"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == config.OWNER_ID:
                    text = f"ᴄᴀɴɴᴏᴛ ᴇᴄʜᴏ ᴏɴ ᴏᴡɴᴇʀ !"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDOERS:
                    text = f"ᴄᴀɴɴᴏᴛ ᴇᴄʜᴏ ᴏɴ ꜱᴜᴅᴏᴜꜱᴇʀ !"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in ECHOUSER:
                     await event.reply("**» ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴇᴄʜᴏʟɪꜱᴛ !!**")
                     return
            ECHOUSER.append(user_id) 
            await event.reply("ᴇᴄʜᴏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")
     else:
         await event.reply(usage)

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : RM ECHO**\n\nCommand :\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDOERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            if int(user_id) in ECHOUSER:
                ECHOUSER.remove(user_id) 
                await event.reply("ᴇᴄʜᴏ ʀᴇᴍᴏᴠᴇᴅ  ☑️")
            else:
                await event.reply("ᴜꜱᴇʀ ɴᴏᴛ ɪɴ ᴇᴄʜᴏ ʟɪꜱᴛ !!")
     else:
          await event.reply(usage)


@BOT0.on(events.NewMessage(incoming=True))
@BOT1.on(events.NewMessage(incoming=True))
@BOT2.on(events.NewMessage(incoming=True))
@BOT3.on(events.NewMessage(incoming=True))
@BOT4.on(events.NewMessage(incoming=True))
@BOT5.on(events.NewMessage(incoming=True))
@BOT6.on(events.NewMessage(incoming=True))
@BOT7.on(events.NewMessage(incoming=True))
@BOT8.on(events.NewMessage(incoming=True))
@BOT9.on(events.NewMessage(incoming=True))
async def _(e):
    if e.sender_id in ECHOUSER:
        await asyncio.sleep(0.5)
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
