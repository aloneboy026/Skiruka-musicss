import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "10284859"))
API_HASH = getenv("API_HASH", "b0ad58eb8b845ba0003e0d9ce5fc2196")

BOT_TOKEN = getenv("BOT_TOKEN", "5791761493:AAE0Rk6NScE8h3sXr12ES9W-hoYR1Z9Dnl0")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kittuthemeoe:kiranraj@cluster0.mv6oj.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "600"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001853853435"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "angel music")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5613528193").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY") 
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/its-star-boi/ShizukaXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/its-star-boi/ShizukaXMusic")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/team_comrades")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/mondo_lover")


AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "false")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCp74kggJj__lWkNav5VC8jMGbYsNB7vR0sodWWnonN1ODkMQJj6H3ZKlJwD_kW_99F_n0J4CxFzh3KSGEDUUJLpirRMgFc5S0r2nSc1Ho0zoOK3FQxdRu4QNlHs-gYdDOJA0B_9rhsJq-I9KwzARDeBDSd-mU14tn-xxoesAE3qrNal-NYz9_VqTLzf8O9LtyYENvvJBcN5IZ0MnC1L1FnTohpinefiNahWPQrwZpYF2GXaTjAeBMMVtWpRk37M9EELLgulMJM2xi-YjBg9gjvrYFQ9NuNkJbjrA0Bcjl69-cTwYsXrHaPm1440pF8LLia35ISqPMXjoywUhw5l8KrAAAAAXML5aUA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/202c8e5a57f1f8597fe2a.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/53112d2692ac8d0b499c0.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/866b9268d45ef5647a642.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/abafd51a44a1fe4d6e2e7.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/cbdad34a3e9f42609181c.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/74ca9881e017b55566611.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/9fcb1be4c33005e4b8156.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/fb8503859fff2455202d8.jpg"
