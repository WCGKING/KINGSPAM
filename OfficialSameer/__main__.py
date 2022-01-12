#SAMoeLXSpam By @TheSAMoeL

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from OfficialSameer.utils import load_plugins
import logging
from telethon import events
from . import SAM, SAM2, SAM3, SAM4, SAM5, SAM6, SAM7, SAM8, SAM9, SAM10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "OfficialSameer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("🍌🍌 Deadly Spam Bot Successfully deployed 🍌🍌")
print("Enjoy! Do visit @Deadly_Spam_bot")

if __name__ == "__main__":
    SAM.run_until_disconnected()
    
if __name__ == "__main__":
    SAM2.run_until_disconnected()

if __name__ == "__main__":
    SAM3.run_until_disconnected()
    
if __name__ == "__main__":
    SAM4.run_until_disconnected()

if __name__ == "__main__":
    SAM5.run_until_disconnected()
    
if __name__ == "__main__":
    SAM6.run_until_disconnected()
    
if __name__ == "__main__":
    SAM7.run_until_disconnected()

if __name__ == "__main__":
    SAM8.run_until_disconnected()
    
if __name__ == "__main__":
    SAM9.run_until_disconnected()

if __name__ == "__main__":
    SAM10.run_until_disconnected()    
