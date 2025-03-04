from pyrogram import Client, filters

def setup_handlers(app: Client):
    @app.on_message(filters.command("trending"))
    def trending_songs(client, message):
        songs = ["Song 1", "Song 2", "Song 3"]
        message.reply("\n".join(songs))
