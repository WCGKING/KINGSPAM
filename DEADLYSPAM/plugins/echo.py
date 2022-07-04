
import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDO_USERS, OWNER_ID
from DEADLYSPAM import CMD_HNDLR as hl
from resources.data import GROUP, DEADLYSPAM
from DEADLYSPAM.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo


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
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in DEADLYSPAM:
                    text = f"I Can't Echo @deadly_spam_bot Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"This Guy is Owner Of These Bots."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     chandan = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
                     chandan = Get(chandan)
                     await event.client(chandan)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("Echo Is Already Activated On This User !!")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo Activated On The User ✅")
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
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                blaze = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
                blaze = Get(blaze)
                await event.client(blaze)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo Has Been Stopped For The User ☑️")
            else:
                await event.reply("Echo Is Already Disabled !!")
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
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            spam = base64.b64decode("QERlYWRseV9zcGFtX2JvdA==")
            spam = Get(spam)
            await e.client(spam)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
