from instagrapi import Client
import time
import random

# Login with your session ID
cl = Client()
cl.login_by_sessionid("75899522429%3AKKhY3DfHuLgqp7%3A8%3AAYdVPKkEXV9h4j8392QoktVNjM-ghHZweTROm_1GLg")  # 👈 Replace with your real session ID

# Message templates with safe character limits (max ~1000 chars)
reply_templates = [
    ("SUBANSH L9 PE_____// " * 20).strip(),
    ("BHAG MATT____////// " * 20).strip(),
    ("TERYY GND FADU BACHE ______/// " * 18).strip(),
    ("CHAL DUMM LAGA HAHAHAAH __///// " * 18).strip()
]

# Get the top group chat ID
def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# Main auto spam function
def start_gc_autospam():
    gc_thread_id = get_gc_thread_id()
    if not gc_thread_id:
        print("❌ Group chat not found.")
        return

    print(f"🚀 Spamming started in GC: {gc_thread_id}")

    while True:
        try:
            msg = random.choice(reply_templates)
            cl.direct_answer(gc_thread_id, msg)
            print(f"✔️ Sent spam: {msg[:40]}...")  # Preview
            time.sleep(random.randint(25, 40))  # Safe delay between messages
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# Start the bot
start_gc_autospam()
