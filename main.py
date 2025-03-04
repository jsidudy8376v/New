from pyrogram import Client, filters
import config
from handlers import moderation, downloader, utilities, entertainment, tracking, reactions, owner_panel, ai_system, music, events, security_tools, smart_gadgets

app = Client(
    "NeerajProBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# सभी फीचर लोड करना
moderation.setup_handlers(app)
downloader.setup_handlers(app)
utilities.setup_handlers(app)
entertainment.setup_handlers(app)
tracking.setup_handlers(app)
reactions.setup_handlers(app)
owner_panel.setup_handlers(app)
ai_system.setup_handlers(app)
music.setup_handlers(app)
events.setup_handlers(app)
security_tools.setup_handlers(app)
smart_gadgets.setup_handlers(app)

print("✅ NeerajPro Bot Started Successfully!")
app.run()