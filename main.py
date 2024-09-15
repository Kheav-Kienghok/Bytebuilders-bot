from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import requests
import asyncio
import time
import os

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

TOKEN: Final = TELEGRAM_API_TOKEN
BOT_USERNAME: Final = '@ByteBuilders_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! How can I assist you?')

# Handle the bot's response based on the incoming message
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> str:
    try:
        if len(text) <= 10:
            if 'noted' in text.lower() or 'done' in text.lower():
                # If "noted" or "done" is detected, just send a reaction and don't send a reply
                await send_reaction(update, context)
    except Exception as e:
        print(f"Error in handle_response: {e}")
    return None  # No text reply

# Send a reaction (emoji) to the previous message
async def send_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        api_url = f"https://api.telegram.org/bot{TOKEN}/setMessageReaction"  # Adjust the API if needed for reactions

        # Define the parameters for the request
        params = {
            'chat_id': chat_id,  # Dynamic chat ID from the Update object
            'message_id': message_id,  # Dynamic message ID from the Update object
            'reaction': '[{"type":"emoji", "emoji":"❤️"}]'  # Emoji reaction
        }

        # Make the request
        response = requests.post(api_url, params=params)
        print(response.json())  # Print response for debugging

    except Exception as e:
        print(f"Error in send_reaction: {e}")

# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = await handle_response(update, context, new_text)
        else:
            return  # Do nothing if bot is not mentioned
    else:
        response: str = await handle_response(update, context, text)

    # If there's a response text, send it (skip sending message if the response is None)
    if response:
        print('Bot:', response)
        await update.message.reply_text(response)

# Log and handle errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

def run_bot():
    # Start the bot
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')

    try:
        app.run_polling(poll_interval=3, timeout=12)
    except Exception as e:
        print(f"Bot crashed with error: {e}")
        time.sleep(5)  # Wait before restarting
        run_bot()  # Restart the bot after a crash

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())  # Ensure that we run in a clean asyncio environment
    except KeyboardInterrupt:
        print("Bot stopped manually.")