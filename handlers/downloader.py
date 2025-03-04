import yt_dlp
from pyrogram import Client, filters

def setup_handlers(app: Client):
    @app.on_message(filters.command("song"))
    def song(client, message):
        query = " ".join(message.command[1:])
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'quiet': True}) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            message.reply_audio(info['url'], caption=f"🎶 {info['title']}")
