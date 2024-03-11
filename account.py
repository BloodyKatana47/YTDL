from ast import literal_eval
from os import getenv, remove

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytube import YouTube

from database import Database

load_dotenv()
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
BOT_ID = getenv('BOT_ID')

app = Client(name="my_account", api_id=API_ID, api_hash=API_HASH)
db = Database('users.db')


@app.on_message(filters.user(int(BOT_ID)))
async def download(client, message):
    json_data = literal_eval(message.text)
    user_id = json_data['id']
    source = json_data['source']
    db.set_status(user_id=user_id, status=1)

    if source == 'yt':
        try:
            # If use_oauth set True - authentication link will be displayed
            yt = YouTube(message.text, use_oauth=True, allow_oauth_cache=True)
            # D:\Python Projects\Мои работы\YTDL\venv\Lib\site-packages\pytube\innertube.py
            # 223 line
            # def __init__(self, client='ANDROID_MUSIC', use_oauth=False, allow_cache=True):
            # to
            # def __init__(self, client='ANDROID', use_oauth=False, allow_cache=True):
            video_stream = yt.streams.get_highest_resolution()
            filename = f'{json_data["file_name"]}.mp4'

            video_stream.download(output_path='downloads', filename=filename)
            await app.send_video(chat_id=int(BOT_ID), video=open(f'downloads/{filename}', 'rb'), caption=message.text)
            remove(f'downloads/{filename}')

            db.set_status(user_id=user_id, status=0)
        except:
            await app.send_message(chat_id=int(BOT_ID), text=message.text)

            db.set_status(user_id=user_id, status=0)
    elif source == 'ig':
        pass


app.run()
