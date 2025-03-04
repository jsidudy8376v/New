from pyrogram import Client, filters
from config import BANNED_WORDS, PHISHING_LINKS

def setup_handlers(app: Client):
    @app.on_message(filters.group & filters.text)
    def auto_moderate(client, message):
        if any(word in message.text.lower() for word in BANNED_WORDS):
            message.delete()
            message.reply("❌ Banned Word Detected!")
        elif any(link in message.text for link in PHISHING_LINKS):
            message.delete()
            message.reply("⚠️ Phishing Link Detected!")

    @app.on_message(filters.sticker)
    def sticker_to_image(client, message):
        file = client.download_media(message)
        message.reply_photo(file, caption="Sticker converted to image.")