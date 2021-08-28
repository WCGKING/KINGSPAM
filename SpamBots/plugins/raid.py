
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS, RAID, RRAID

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}



@UstaD.on(events.NewMessage(pattern="/raid"))
@UstaD2.on(events.NewMessage(pattern="/raid"))
@UstaD3.on(events.NewMessage(pattern="/raid"))
@UstaD4.on(events.NewMessage(pattern="/raid"))
@UstaD5.on(events.NewMessage(pattern="/raid"))
@UstaD6.on(events.NewMessage(pattern="/raid"))
@UstaD7.on(events.NewMessage(pattern="/raid"))
@UstaD8.on(events.NewMessage(pattern="/raid"))
@UstaD9.on(events.NewMessage(pattern="/raid"))
@UstaD10.on(events.NewMessage(pattern="/raid"))
async def spam(e):  
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Ustad) == 2:
            message = str(Ustad[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Ustad[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(Ustad[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@UstaD.on(events.NewMessage(incoming=True))
@UstaD2.on(events.NewMessage(incoming=True))
@UstaD3.on(events.NewMessage(incoming=True))
@UstaD4.on(events.NewMessage(incoming=True))
@UstaD5.on(events.NewMessage(incoming=True))
@UstaD6.on(events.NewMessage(incoming=True))
@UstaD7.on(events.NewMessage(incoming=True))
@UstaD8.on(events.NewMessage(incoming=True))
@UstaD9.on(events.NewMessage(incoming=True))
@UstaD10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@UstaD.on(events.NewMessage(pattern="/replyraid"))
@UstaD2.on(events.NewMessage(pattern="/replyraid"))
@UstaD3.on(events.NewMessage(pattern="/replyraid"))
@UstaD4.on(events.NewMessage(pattern="/replyraid"))
@UstaD5.on(events.NewMessage(pattern="/replyraid"))
@UstaD6.on(events.NewMessage(pattern="/replyraid"))
@UstaD7.on(events.NewMessage(pattern="/replyraid"))
@UstaD8.on(events.NewMessage(pattern="/replyraid"))
@UstaD9.on(events.NewMessage(pattern="/replyraid"))
@UstaD10.on(events.NewMessage(pattern="/replyraid"))
async def _(e):
    global que
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Ustad[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@UstaD.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD2.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD3.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD4.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD5.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD6.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD7.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD8.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD9.on(events.NewMessage(pattern="/dreplyraid"))
@UstaD10.on(events.NewMessage(pattern="/dreplyraid"))
async def _(e):
    global que    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Ustad[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
