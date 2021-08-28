from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@UstaD.on(events.NewMessage(pattern="/restart"))
@UstaD2.on(events.NewMessage(pattern="/restart"))
@UstaD3.on(events.NewMessage(pattern="/restart"))
@UstaD4.on(events.NewMessage(pattern="/restart"))
@UstaD5.on(events.NewMessage(pattern="/restart"))
@UstaD6.on(events.NewMessage(pattern="/restart"))
@UstaD7.on(events.NewMessage(pattern="/restart"))
@UstaD8.on(events.NewMessage(pattern="/restart"))
@UstaD9.on(events.NewMessage(pattern="/restart"))
@UstaD10.on(events.NewMessage(pattern="/restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🤖𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐄𝐃🤖\n🔰𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐓𝐈𝐋𝐋 𝐈𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐒...."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await UstaD.disconnect()
        except Exception:
            pass
        try:
            await UstaD2.disconnect()
        except Exception:
            pass
        try:
            await UstaD3.disconnect()
        except Exception:
            pass
        try:
            await UstaD4.disconnect()
        except Exception:
            pass
        try:
            await UstaD5.disconnect()
        except Exception:
            pass
        try:
            await UstaD6.disconnect()
        except Exception:
            pass
        try:
            await UstaD7.disconnect()
        except Exception:
            pass
        try:
            await UstaD8.disconnect()
        except Exception:
            pass
        try:
            await UstaD9.disconnect()
        except Exception:
            pass
        try:
            await UstaD10.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
