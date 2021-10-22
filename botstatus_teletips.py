#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

MORE = """
**📊 <u>MORE BOTS:</u>**
• @AlterPendragonBot
• @AsunaDevRobot
• @Mio_Probot
• @MrZackBot
• @NekopoiHenBot
• @TgraBot
• @TokisakiRobot
• @TosakaRobot
• @YuitoRobot
• @YuKaYaBot
• @zUnzipBot
"""

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_teletips = f"📊 **<u>YOGA BOT STATUS</u>**\n\n**💬 Channel**: Spread Networks" #{CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.message_id
                        await asyncio.sleep(10)
                        zzz_teletips = await app.get_history(bot, limit = 1)
                        for ccc in zzz_teletips:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: Offline ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Warn! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xxx_teletips += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: Online ✅"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += MORE
                xxx_teletips += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Auto updates every 24 hours,\n🧑‍💻 Powered by @Yoga_CIC.</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(86400)
                        
app.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
