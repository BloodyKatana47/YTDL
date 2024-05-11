from aiogram.utils.markdown import hlink, hbold

VIDEO_CAPTION: str = f'''
{hbold('✅ Скачано с помощью ')}{hlink(title='YTDL | Скачать с Youtube/Youtube Shorts',
                                      url='https://t.me/yt_shorts_download_bot')}
💚 Спасибо за использование нашего бота!'''

START_MESSAGE: str = f"""👋 {hbold('Вас приветствует бот для загрузки видео.')}
\nИмеется возможность загрузки из следующих источников:
❤ {hbold('YouTube')}
❤ {hbold('YouTube Shorts')}"""

LINK_NOT_FOUND: str = f'''✋ {hbold("Упс, ссылка не найдена.")}'''

MULTIPLE_LINKS: str = f'''🛑 {hbold("Пожалуйста. отправьте ссылку только на одно видео.")}'''

DOWNLOADING_STARTED: str = f'''✔ {hbold("Отлично, загрузка видео началась.")}'''

WAIT: str = f"""🛑 {hbold('Пожалуйста, дождитесь пока загрузится предыдущее видео.')}"""
