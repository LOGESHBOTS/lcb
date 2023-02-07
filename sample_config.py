import os
from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start

API_ID = int(os.getenv("API_ID", "14553761"))
API_HASH = os.environ.get("API_HASH", "a1cab49dcdfd2eb3bea5e5a552c5d479")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("604152966")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "604152966")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(604152966)


#  Optionnal variables

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "KPSLink") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/496e7ae942556eb072ab6.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"