class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6961287189"
    sudo_users = "6961287189", "7078181502"
    GROUP_ID =-1002181724288 -
    TOKEN = "7367511450:AAFb78v-duwLXS0IZraAU33CEPxdg5SVCs0"
    mongo_url = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "animehkjy"
    UPDATE_CHAT = "waifebot_supoort"
    BOT_USERNAME = "Collectionwaife_bot"
    CHARA_CHANNEL_ID = "-1002220612751"
    api_id = 23255238
    api_hash = "009e3d8c1bdc89d5387cdd8fd182ec15"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
