import glob
from pathlib import Path
from SpamBots.utils import load_plugins
import logging
from . import UstaD, UstaD2, UstaD3, UstaD5 , UstaD6, UstaD7, UstaD8, UstaD9, UstaD10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "SpamBots/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @USTAD_SPAM_BOTS")

if __name__ == "__main__":
    UstaD.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD2.run_until_disconnected()

if __name__ == "__main__":
    UstaD3.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD4.run_until_disconnected()

if __name__ == "__main__":
    UstaD5.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD6.run_until_disconnected()

if __name__ == "__main__":
    UstaD7.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD8.run_until_disconnected()

if __name__ == "__main__":
    UstaD9.run_until_disconnected()
    
if __name__ == "__main__":
    UstaD10.run_until_disconnected()

