from pyrogram import Client, filters
from config import OWNER_ID

def setup_handlers(app: Client):
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    def broadcast(client, message):
        text = " ".join(message.command[1:])
        for member in client.get_chat_members(message.chat.id):
            client.send_message(member.user.id, text)