from pyrogram import Client, filters
import random

def setup_handlers(app: Client):
    @app.on_message(filters.command("truth"))
    def truth(client, message):
        truths = ["What's your biggest secret?", "Who do you have a crush on?"]
        message.reply(random.choice(truths))

    @app.on_message(filters.command("dare"))
    def dare(client, message):
        dares = ["Send a selfie right now!", "Text your crush 'I love you'."]
        message.reply(random.choice(dares))