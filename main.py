# main.py

from instagrapi import Client
import time
import random
import uuid
import itertools
from threading import Thread
from flask import Flask

# 🔐 Flask webserver (keep alive)
app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 Insta Spam Bot Running..."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# 🔐 Login to Instagram
cl = Client()
cl.login_by_sessionid("75899522429%3AKKhY3DfHuLgqp7%3A8%3AAYdVPKkEXV9h4j8392QoktVNjM-ghHZweTROm_1GLg")

# 💬 Safe spam messages
reply_templates = [
    ("SUBANSH L9 PE_____// " * 20).strip(),
    ("BHAG MATT____////// " * 20).strip(),
    ("TERYY GND FADU BACHE ______/// " * 18).strip(),
    ("CHAL DUMM LAGA HAHAHAAH __///// " * 18).strip()
]

msg_cycle = itertools.cycle(reply_templates)

# 🔍 Top GC
def get_gc_thread_id():
    threads = cl.direct_threads(amount=5)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# 🔁 Spam loop
def start_gc_autospam():
    gc_thread_id = get_gc_thread_id()
    if not gc_thread_id:
        print("❌ Group chat not found.")
        return

    print(f"🚀 Spamming started in GC: {gc_thread_id}")

    while True:
        try:
            msg_base = next(msg_cycle)
            unique_msg = f"{msg_base}\n\nID: {uuid.uuid4()}"
            cl.direct_answer(gc_thread_id, unique_msg)
            print(f"✔️ Sent: {unique_msg[:40]}...")
            time.sleep(random.randint(25, 40))
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# ▶️ Start threads
if __name__ == '__main__':
    Thread(target=run_flask).start()
    Thread(target=start_gc_autospam).start()
