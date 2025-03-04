from pyrogram import Client, filters
from config import DEFAULT_WELCOME_MESSAGE

def setup_handlers(app: Client):
    @app.on_message(filters.new_chat_members)
    def welcome(client, message):
        for user in message.new_chat_members:
            message.reply(DEFAULT_WELCOME_MESSAGE.format(name=user.first_name, group=message.chat.title))