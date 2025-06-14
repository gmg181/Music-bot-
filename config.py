import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Ironmanhindigaming")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","irotechmusicbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME","IRO MUSIC")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002311769574))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5909658683))


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", '30DxNexGenBotsbe462b') # youtube song api key
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/gmg181/Music-bot-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN","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")  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/irotechlab")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ironmanhindigming1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/qk2t0t.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/fcawaj.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
STATS_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/fcawaj.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/fcawaj.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
