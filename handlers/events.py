from pyrogram import Client, filters
from config import BIRTHDAYS
from datetime import datetime

def setup_handlers(app: Client):
    @app.on_message(filters.text)
    def birthday_wish(client, message):
        today = datetime.now().strftime("%m-%d")
        for user, date in BIRTHDAYS.items():
            if date == today:
                client.send_message(message.chat.id, f"Happy Birthday {user}! 🎂")
