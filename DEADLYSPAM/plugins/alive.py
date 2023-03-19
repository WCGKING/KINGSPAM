import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph/file/46d7b153e36f36454269e.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝗙𝗖𝗥 𝗫 𝗧𝗘𝗔𝗠 𝗔𝗚𝗢𝗥𝗔 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ғᴄʀ x ᴛᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/aboutagora"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/do_jism_ek_jaan_op")], [Button.url("• ʀᴇᴘᴏ •", "https://github.com/Team-Deadly/DEADLY-SPAMBOT")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ғᴄʀ x ᴛᴇᴀᴍ ᴀɢᴏʀᴀ-ꜱᴘᴀᴍʙᴏᴛ!**") 
