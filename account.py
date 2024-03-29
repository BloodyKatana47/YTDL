import urllib.error
from ast import literal_eval
from os import getenv, remove, mkdir

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytube import YouTube
from pytube.innertube import _default_clients

from database import Database

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

load_dotenv()
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
BOT_ID = getenv('BOT_ID')

app = Client(name="my_account", api_id=API_ID, api_hash=API_HASH)
db = Database('users.db')

try:
    mkdir('downloads')
except FileExistsError:
    pass


@app.on_message(filters.user(int(BOT_ID)))
async def download(client, message):
    json_data = literal_eval(message.text)
    user_id = json_data['id']
    db.set_status(user_id=user_id, status=1)

    try:
        yt = YouTube(json_data['url'], use_oauth=True, allow_oauth_cache=True)
        video_stream = yt.streams.get_highest_resolution()
        filename = f'{json_data["file_name"]}.mp4'

        video_stream.download(output_path='downloads', filename=filename)
        await app.send_video(chat_id=int(BOT_ID), video=open(f'downloads/{filename}', 'rb'), caption=message.text)
        remove(f'downloads/{filename}')

        db.set_status(user_id=user_id, status=0)
    except urllib.error.HTTPError:
        await app.send_message(chat_id=int(BOT_ID), text=message.text)

        db.set_status(user_id=user_id, status=0)


app.run()
