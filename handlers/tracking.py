from pyrogram import Client, filters

def setup_handlers(app: Client):
    @app.on_message(filters.left_chat_member)
    def left_log(client, message):
        message.reply(f"User {message.left_chat_member.first_name} has left.")