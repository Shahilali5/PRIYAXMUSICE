import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21071632
API_HASH = "6702b2136420ebac56753d8fad96a80d"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8162481586:AAERyZk6Ax3PQxHvqekT4ZO87EVValt6iRY"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb://devilmods:devilmods@<hostname>/?ssl=true&replicaSet=atlas-ovbijr-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Shahul"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002414808261

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8129810243

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/priyaxmusicepro"
SUPPORT_GROUP = "https://t.me/PriyaXmuscie"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFBhxAAdRJfpHETqTd87rk_Tx19YiepusFhB64iwZOcfAyIa-D2c556MzHget7dDcG-T8XwttRTX7URGxiQBO8_ctA8wQYrd815FPNbPbWA38-rgeigAuDVfF1NSTPoldf289KhZF87G1vBbtE5mSwoY1WynDKYI8uurBjY3UTabPpeVVO6zNP3T7P6w7pJkmSeuyr6Jn3EtgOfr6UjjWIg1wyq5AoJ57aWxg_N7mBYW86m-cZiWZcow-6NDaX9gpehEARTW7KlrqrBVQSGxH3oYUoUGE1RynAD8q4Kxv0nfmZUy5mLM0EK06OyHsow_ZGrujyzLEt1VV7bImqBytazJP92KQAAAAGbg2ybAA"
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


START_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"

PING_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
STATS_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
STREAM_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/45ca21a91cd22b2242c01-28df7b79e989512360.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
