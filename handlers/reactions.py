from pyrogram import Client, filters

reactions = {
    "hello": "Hello! How are you?",
    "bye": "Goodbye! See you soon!"
}

def setup_handlers(app: Client):
    @app.on_message(filters.text)
    def auto_reply(client, message):
        reply = reactions.get(message.text.lower())
        if reply:
            message.reply(reply)