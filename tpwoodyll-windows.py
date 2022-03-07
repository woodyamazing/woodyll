keybind = "9" #set your keybind here


import pyperclip as pc
import keyboard as k
import time

while True:
    k.wait(keybind)
    coords = pc.paste()

    k.send('alt+tab')
    time.sleep(0.5)
    k.send("t")
    time.sleep(0.05)
    k.send("backspace")
    k.write("/tpll "+ coords)
    k.press("enter")
    time.sleep(0.1)
    k.press_and_release("t")
    time.sleep(0.05)
    k.send("backspace")
    k.write("/up 0")
    k.press("enter")
    k.send('alt+tab')
