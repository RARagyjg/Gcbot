from instagrapi import Client
import time
import random
import uuid
import itertools

# 🔐 Login with session ID
cl = Client()
cl.login_by_sessionid("75899522429%3AKKhY3DfHuLgqp7%3A8%3AAYdVPKkEXV9h4j8392QoktVNjM-ghHZweTROm_1GLg")  # 👈 Replace with your session ID

# 💬 Message templates with safe limits
reply_templates = [
    ("SUBANSH L9 PE_____// " * 20).strip(),
    ("BHAG MATT____////// " * 20).strip(),
    ("TERYY GND FADU BACHE ______/// " * 18).strip(),
    ("CHAL DUMM LAGA HAHAHAAH __///// " * 18).strip()
]

# 🔁 Use cycle to rotate messages
msg_cycle = itertools.cycle(reply_templates)

# 🧠 Find first group chat
def get_gc_thread_id():
    threads = cl.direct_threads(amount=5)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# 🚀 Start spamming loop
def start_gc_autospam():
    gc_thread_id = get_gc_thread_id()
    if not gc_thread_id:
        print("❌ Group chat not found.")
        return

    print(f"🚀 Spamming started in GC: {gc_thread_id}")

    while True:
        try:
            msg_base = next(msg_cycle)
            unique_msg = f"{msg_base}\n\nID: {uuid.uuid4()}"  # Har msg alag banane ke liye
            cl.direct_answer(gc_thread_id, unique_msg)
            print(f"✔️ Sent: {unique_msg[:40]}...")
            time.sleep(random.randint(25, 40))  # Safe delay
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# ▶️ Start
start_gc_autospam()
