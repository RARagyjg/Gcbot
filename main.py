from instagrapi import Client
import time
import random
from keep_alive import keep_alive

keep_alive()

cl = Client()
cl.login_by_sessionid("75538953450%3An9Gkv6yRbGwzFJ%3A11%3AAYfdsUrW8fPD-Ue_dzbp5sApNc9OiXCfDWzPmm_Low")  # 🔐 Apna session ID daalo

me_id = cl.user_id
my_username = cl.username
print(f"🤖 Logged in as @{my_username} (ID: {me_id})")

# ✅ Message reply templates (edit if you want)
reply_templates_master = [
    """𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐊𝐔𝐖𝐀𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐀 𝐀𝐒𝐒 𝐇𝐎𝐋𝐄 𝐁𝐀𝐇𝐔𝐓 𝐓𝐈𝐆𝐇𝐓 𝐇_________________________________________________/
𝐍𝐈𝐂𝐊 𝐊𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐈 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐃𝐁𝐔 𝐌𝐀𝐑𝐓𝐈 𝐇__________________________________________________/""",
"""𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/

𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/

𝗡𝗜𝗖𝗞 𝗧𝗘𝗥𝗜 𝟭𝟱 𝗦𝗔𝗔𝗟 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗞𝗢 𝗥𝗢𝗭 𝗠𝗘 𝗢𝗬𝗢 𝗠𝗘 𝗟𝗘𝗝𝗔𝗞𝗔𝗥 𝟰 𝗚𝗛𝗔𝗡𝗧𝗘 𝗖𝗛#𝗢𝗗𝗧𝗔 𝗛𝗨 ____________________________________________________/
𝗡𝗜𝗖𝗞 𝗞𝗜 𝗕𝗛𝗘𝗡 𝗢𝗬𝗢 𝗠𝗘 𝗥𝗢𝗭 𝗠𝗔𝗥𝗪𝗔𝗧𝗜___________________________________________/"""
]

# 🧠 Maintain last message replied for each user
last_msg_id_by_user = {}

def get_next_reply(username, history):
    # Filter replies jo already iss user ko bheje gaye ho
    possible_replies = [r for r in reply_templates_master if r not in history]
    if not possible_replies:
        history.clear()
        possible_replies = reply_templates_master.copy()
    reply = random.choice(possible_replies)
    history.add(reply)
    return reply.replace("{user}", username)

user_reply_history = {}

def auto_reply():
    while True:
        try:
            threads = cl.direct_threads(amount=1)

            for thread in threads:
                if not thread.messages:
                    continue

                latest_msg = thread.messages[0]

                # Apna msg ignore karo
                if latest_msg.user_id == me_id:
                    continue

                user_id = latest_msg.user_id
                username = cl.user_info(user_id).username

                # Agar same msg pe already reply kar chuke ho, skip karo
                if last_msg_id_by_user.get(user_id) == latest_msg.id:
                    continue

                # User history init if not exists
                if user_id not in user_reply_history:
                    user_reply_history[user_id] = set()

                # 📨 Generate new random reply
                reply = get_next_reply(username, user_reply_history[user_id])

                try:
                    cl.direct_answer(thread.id, reply)
                    print(f"✔️ Replied to @{username}: {reply}")
                    last_msg_id_by_user[user_id] = latest_msg.id
                    time.sleep(random.randint(0, 10))
                except Exception as e:
                    print(f"⚠️ Failed to reply in thread {thread.id}: {e}")

            time.sleep(random.randint(0, 10))

        except Exception as err:
            print(f"🚨 Main loop error: {err}")
            time.sleep(random.randint(0, 10))

# 🚀 Start bot
auto_reply()
                    
