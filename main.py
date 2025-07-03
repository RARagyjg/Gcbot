from instagrapi import Client
import time
from keep_alive import keep_alive

# 🟢 Start KeepAlive server for Replit 24/7
keep_alive()

# 🔐 Login with Session ID (replace this)
cl = Client()
cl.login_by_sessionid("75538953450%3A5Si93RWP2kKd9A%3A22%3AAYcl9Rn6O_jHhyGFlRdyLJWLOIb29iPUDDnBcyHdRA")

# 🤖 Bot Info
me_id = cl.user_id
print(f"🤖 Bot running as: {cl.username} (User ID: {me_id})")

# ✅ To avoid replying again to the same message
replied_msg_ids = set()

def auto_reply():
    while True:
        threads = cl.direct_threads(amount=1)

        for thread in threads:
            if not thread.messages:
                continue

            for msg in thread.messages[:1]:  # Last 5 msgs check kare
                if msg.id in replied_msg_ids:
                    continue  # Already replied

                if msg.user_id == me_id:
                    continue  # Apne msg skip

                try:
                    # ✉️ Reply to the same thread (GC or DM)
                    cl.direct_answer(thread.id, "𝗧𝗘𝗥𝗜 𝗠𝗔 𝗞𝗜 𝗖𝗛#𝗧 𝗙𝗔𝗗 𝗗𝗨 𝗧𝗘𝗔𝗠 𝗗𝗘𝗩𝗜𝗟😂")
                    print(f"✔️ Replied to user {msg.user_id} in thread {thread.id}")
                    replied_msg_ids.add(msg.id)

                except Exception as e:
                    print(f"⚠️ Error replying to thread {thread.id}: {e}")

        time.sleep(20)

auto_reply()