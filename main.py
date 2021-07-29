from instabot import Instabot
from Secure import user,password

bot = Instabot(user,password)
bot.login()
bot.downloaduser("instagram_user")