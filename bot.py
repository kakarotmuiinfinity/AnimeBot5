import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"

async def start(update: Update, context):
    # Send a 🔥 reaction
    await update.message.reply_text("🔥")
    
    # Send a sticker with the specified sticker ID
    sticker_message = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker="CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA")
    
    # Wait for 2 seconds before deleting the sticker
    await asyncio.sleep(2)
    
    # Delete the sticker
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sticker_message.message_id)

if __name__ == "__main__":
    # Initialize the bot application
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Start the bot
    application.run_polling()
  
