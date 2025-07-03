from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75538953450%3At24V1GN8twnQlL%3A23%3AAYeJih0gT5ef8EC9VzwD6mGXhB95x0AONekxpj9Otg")  # <-- yahan apna session id daal

# 🔄 Group name list
gc_names = [
    "NICK TERI MA KI CH00T DE💗",
    "NICK KI MA BOXDI FADU💚",
    "NICK TERYY BHEN KI BOOR FADU❤️",
    "NICK TERI MA KI CH00T DILLA",
    " NICK TERA BAAP AUJLA HERE❣️",
    "NICK KI MA CHUDGYI RE 💜"
]

# 🆔 Auto detect sabse upar wala group chat
def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

def start_name_spam():
    gc_thread_id = get_gc_thread_id()
    if not gc_thread_id:
        print("❌ Group chat not found.")
        return

    print(f"🎯 Spamming group: {gc_thread_id}")

    while True:
        try:
            new_name = random.choice(gc_names)
            cl.direct_thread_rename(gc_thread_id, new_name)
            print(f"✔️ Changed name to: {new_name}")
            time.sleep(random.randint(15, 30))  # safe delay
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(random.randint(10, 20))

start_name_spam()
