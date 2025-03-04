import openai
from pyrogram import Client, filters
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def setup_handlers(app: Client):
    @app.on_message(filters.command("ask"))
    def ask_gpt(client, message):
        query = " ".join(message.command[1:])
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
        )
        message.reply(response['choices'][0]['message']['content'])
