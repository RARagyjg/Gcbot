from instagrapi import Client
import time
import random

cl = Client()
cl.login_by_sessionid("70016257168%3ATjFKaqSuFT6poD%3A7%3AAYd66AgjBaUKl7K16jHtj3SvVPedLFlSkWWW5VfRqA")  # Replace with actual session ID

def get_gc_thread_id():
    threads = cl.direct_threads(amount=1)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

gc_thread_id = get_gc_thread_id()

if gc_thread_id:
    while True:
        try:
            cl.direct_answer(gc_thread_id, "NICK TERYYY MAAA KAAAAAA BHOOOOOSSDAAAAAA FAAADUNGAAAAAA RANDDIIIKKEEEEE BEEEEEEEEJJJJJJ______////NICK TERYYY MAAA KAAAAAA BHOOOOOSSDAAAAAA FAAADUNGAAAAAA RANDDIIIKKEEEEE BEEEEEEEEJJJJJJ______////NICK TERYYY MAAA KAAAAAA BHOOOOOSSDAAAAAA FAAADUNGAAAAAA RANDDIIIKKEEEEE BEEEEEEEEJJJJJJ______////NICK TERYYY MAAA KAAAAAA BHOOOOOSSDAAAAAA FAAADUNGAAAAAA RANDDIIIKKEEEEE BEEEEEEEEJJJJJJ______////")
            print("✔️ Sent to GC!")
            time.sleep(random.randint(60, 80))
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(random.randint(60, 80))
else:
    print("❌ Group chat not found.")
