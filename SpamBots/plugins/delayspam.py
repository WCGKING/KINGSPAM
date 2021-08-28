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



@UstaD.on(events.NewMessage(pattern="/delayspam"))
@UstaD2.on(events.NewMessage(pattern="/delayspam"))
@UstaD3.on(events.NewMessage(pattern="/delayspam"))
@UstaD4.on(events.NewMessage(pattern="/delayspam"))
@UstaD5.on(events.NewMessage(pattern="/delayspam"))
@UstaD6.on(events.NewMessage(pattern="/delayspam"))
@UstaD7.on(events.NewMessage(pattern="/delayspam"))
@UstaD8.on(events.NewMessage(pattern="/delayspam"))
@UstaD9.on(events.NewMessage(pattern="/delayspam"))
@UstaD10.on(events.NewMessage(pattern="/delayspam"))
async def spam(e):    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Ustad = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Ustadsexy = Ustad[1:]
        if len(Ustadsexy) == 2:
            message = str(Ustadsexy[1])
            counter = int(Ustadsexy[0])
            sleeptime = float(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Ustadsexy[0])
            sleeptime = float(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Ustadsexy[0])
            sleeptime = float(Ustad[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
