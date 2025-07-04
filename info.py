import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", False)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['29870283'])
API_HASH = environ['e803aa1882327dc35bb0276279a849c2']
BOT_TOKEN = environ['7783558366:AAEpRjXh9GdOeNyPWM0bt5K8UPS1arPkTk4']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://telegra.ph/file/0507c8ee38765648de521.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6522991984').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002687418207').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '-1002162269855').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "capal90951")
DATABASE_NAME = environ.get('DATABASE_NAME', "mongodb+srv://capal90951:Ea5ixpHnXwd1dvop@cluster0.vimg7oq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', 'HII 👋 {user}\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', 'Please Join both Updates Channel to use this Bot!')
RemoveBG_API = environ.get("RemoveBG_API", "taF9K5WQVgN3tdsnjuYhg7EN")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}\n\nPlease Join Updates Channel to use this Bot!")
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'motumovies')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>📂Fɪʟᴇɴᴀᴍᴇ :{file_name}</b>") 
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>𝗤𝘂𝗲𝗿𝘆: {query}</b> \n‌𝗜𝗠𝗗𝗯 𝗗𝗮𝘁𝗮:\n\n🎬 𝗧𝗶𝘁𝗹𝗲: <a href={url}>{title}</a>\n🎭 𝗚𝗲𝗻𝗿𝗲𝘀: {genres}\n👤 𝗗𝗶𝗿𝗲𝗰𝘁𝗼𝗿: {director}\n👥 𝗖𝗮𝘀𝘁: {cast_names}\n⏰ 𝗥𝘂𝗻𝘁𝗶𝗺𝗲: {runtime}\n📆 𝗬𝗲𝗮𝗿: <a href={url}/releaseinfo>{year}</a>\n📊 𝗥𝗮𝘁𝗶𝗻𝗴: <a href={url}/ratings>{rating}</a> / 10 ⭐\n🔗 𝗜𝗠𝗗𝗕 𝗟𝗶𝗻𝗸: {imdb_link}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002687418207')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

