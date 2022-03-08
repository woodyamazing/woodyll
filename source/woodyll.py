import subprocess
import sys
import importlib
import time
import os
import json

def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("pyperclip")
install("keyboard")

pc = importlib.import_module('pyperclip')
k = importlib.import_module('keyboard')

configFile = __file__[0:-17] + 'config.json'  # path to config file

# load config file
with open(configFile, 'r') as config:
	configData = json.load(config)
	delay = int(configData["delay"])
	keybind = configData["keybind"]
	height = configData["tpll height"]
# detect OS
if os.name == "posix":
	appSwitch = "cmd+tab"

if os.name == "nt":
	appSwitch = "alt+tab"

os.system('cls' if os.name == 'nt' else 'clear')
print("tpwoodyll v1.1 \nReady")

while True:
	k.wait(keybind)

	coords = pc.paste()
	tpll = str("/tpll "+ coords + height)

	k.send(appSwitch)
	time.sleep(delay)
	k.send("esc")
	k.send("t")
	time.sleep(0.1)
	k.send("backspace")
	k.write(tpll)
	k.press("enter")
	time.sleep(0.1)
	k.send("t")
	time.sleep(0.1)
	k.send("backspace")
	k.write("/up 0")
	k.send("enter")
	k.send(appSwitch)

