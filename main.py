from instagrapi import Client
import time
import random

cl = Client()
cl.login_by_sessionid("75899522429%3AKKhY3DfHuLgqp7%3A8%3AAYdVPKkEXV9h4j8392QoktVNjM-ghHZweTROm_1GLg")  # 🔐 Replace with real session ID

def get_gc_thread_id():
    threads = cl.direct_threads(amount=10)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

gc_id = get_gc_thread_id()

# ✅ Only 4 Hardcore Abusive Messages (Safe Wrapped)
messages = [
    "NICK TERYY MAA KI BOXDIII FAAADDD DUGAAA______//// " * 38,
    "NICK TERA BAAPP HU ME SMJHA GWR_____/ " * 39,
    "TERIII MA KI BUR KA KHUN CHUS LUGA _____ " * 36,
    "TERI BHEN KI PANTY UTAR KE CH00T CHUSUGAA _____ " * 40
]

# 🔁 Spam Loop with Safe Randomization
if gc_id:
    count = 0
    while True:
        msg = random.choice(messages)
        cl.direct_send(msg.strip(), [gc_id])
        print(f"📤 Sent message {count + 1}")
        count += 1

        # Random safe delay (15–45 seconds)
        time.sleep(random.randint(15, 45))

        # Cooldown after every 30 messages
        if count % 30 == 0:
            print("⏸️ Cooldown: Sleeping for 2 minutes to avoid detection...")
            time.sleep(120)
