import telebot

Token = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
       bot.reply_to(message, "Hᴇʟʟᴏ {username}✨ Mʏsᴇʟғ {bot_name} Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ? I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!")
    
bot.polling()
