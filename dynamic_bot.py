from telegram import Bot
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler

# Replace with your bot token
BOT_TOKEN = "7590585852:AAFpGHZaDeZCrI850nZtAja133L8QyUMZEY"

# Replace with your intended chat ID
CHAT_ID = "5278908419"

# Function to send a beautifully formatted message with custom arguments
async def send_formatted_text(update, context):
    # Get the argument (if any) passed with the command
    args = context.args
    if args:
        message = f"""👉 <b> Hello <a href="https://t.me/donot/game?startapp=5278908419">{' '.join(args)}</a></b>
🚀 Start your crypto journey today and earn free rewards!"""
    else:
        # Updated default message
        message = """👉 <b> Welcome to our platform! </b>
💎 Claim your free tokens and start earning rewards today. Don't miss out on amazing opportunities! 
<b><a href="https://t.me/donot/game?startapp=5278908419">Click Here to Start</a></b>."""

    # Send the message with link preview disabled
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True  # Disables the link preview
    )

# Function to start the bot
async def start(update, context):
    await update.message.reply_text("Hi! Use /send <message> to send a formatted message with custom text.")

# Main function to run the bot
def main():
    # Create the application instance
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_formatted_text))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
