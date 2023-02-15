import os
from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start

API_ID = int(os.getenv("API_ID", "19010782"))
API_HASH = os.environ.get("API_HASH", "830f2543690bcfb28d27a47d485c1ba4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6267880815:AAFwOu9oRlu405GPJHuFo_36SVZHCPeNRSU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("2037076607")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.vvzdvou.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "2037076607")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(2037076607)


#  Optionnal variables

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001529400690")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "urlshortenlink") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/9926848d6ec146dad83d4.png') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
