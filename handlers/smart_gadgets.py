from pyrogram import Client, filters
import qrcode, io

def setup_handlers(app: Client):
    @app.on_message(filters.command("qr"))
    def qr_generator(client, message):
        text = " ".join(message.command[1:])
        img = qrcode.make(text)
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        bio.seek(0)
        message.reply_photo(bio, caption="Here's your QR Code.")
