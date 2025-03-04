from pyrogram import Client, filters
from config import PHISHING_LINKS

def setup_handlers(app: Client):
    @app.on_message(filters.text)
    def phishing_detector(client, message):
        if any(link in message.text for link in PHISHING_LINKS):
            message.delete()
            message.reply("⚠️ Phishing Link Detected!")
