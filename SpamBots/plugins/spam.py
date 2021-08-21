async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@UstaD.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD2.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD3.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD4.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD5.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD6.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD7.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD8.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD9.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)
@UstaD10.on(
    events.NewMessage(pattern="^/spam", func=lambda e: e.sender_id in SMEX_USERS)
)


async def spam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Ustad) == 2:
            message = str(Ustad[1])
            counter = int(Ustad[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Ustad[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Ustad[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
