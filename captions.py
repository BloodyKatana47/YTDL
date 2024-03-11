from aiogram.utils.markdown import hlink, hbold

VIDEO_CAPTION = f'''
{hbold('✅ Скачано с помощью ')}{hlink(title='YTDL | Скачать с Youtube/Youtube Shorts',
                                      url='https://t.me/yt_shorts_download_bot')}
💚 Спасибо за использование нашего бота!'''

START_MESSAGE = f"""👋 {hbold('Вас приветствует бот для загрузки видео.')}
\nИмеется возможность загрузки из следующих источников:
❤ {hbold('YouTube')}
❤ {hbold('YouTube Shorts')}"""

LINK_NOT_FOUND = f'''✋ {hbold("Упс, ссылка не найдена.")}'''

MULTIPLE_LINKS = f'''🛑 {hbold("Пожалуйста. отправьте ссылку только на одно видео.")}'''

DOWNLOADING_STARTED = f'''✔ {hbold("Отлично, загрузка видео началась.")}'''

WAIT = f"""🛑 {hbold('Пожалуйста, дождитесь пока загрузится предыдущее видео.')}"""
