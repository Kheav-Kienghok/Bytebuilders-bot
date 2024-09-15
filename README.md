# ByteBuilders Bot 🤖❤️

## Overview

**ByteBuilders Bot** is a simple Telegram bot whose sole purpose is to react with a love emoji (`❤️`) when someone sends messages containing the words **"noted"** or **"done"**. The bot has no other functionality or purpose beyond this.

## Features

- Automatically reacts with a `❤️` emoji when it detects the words **"noted"** or **"done"** in a message.
- Responds to the `/start` command with a greeting message.
- Responds to the `/help` command with an assistance prompt.
- Requires **admin privileges** in group chats to ensure it can read messages and respond appropriately.
- No other functionality is provided.

## How It Works

1. The bot listens for messages in a chat (group or private).
    - **Note**: In group chats, the bot must have admin privileges to function correctly.
2. If the message contains the word **"noted"** or **"done"** (case insensitive), it responds with a `❤️` emoji.
3. The bot also responds to the following commands:
    - `/start`: Sends a welcome message.
    - `/help`: Sends an assistance message.
4. If none of these conditions are met, the bot remains silent.

### Example

- **User**: "Noted!"
- **Bot**: ❤️

- **User**: "Done!"
- **Bot**: ❤️

- **User**: `/start`
- **Bot**: "Hello! Thanks for chatting with me!"

- **User**: `/help`
- **Bot**: "Hello! How can I assist you?"

- **User**: "Hello, bot!"
- **Bot**: *(No response)*

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/Kheav-Kienghok/Bytebuilders-bot.git
    ```
2. Navigate to the directory:
    ```bash
    cd Bytebuilders-bot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Telegram bot token by creating a `.env` file with the following content:
    ```bash
    TELEGRAM_API_TOKEN = "your-telegram-bot-token-here"
    ```

5. Run the bot:
    ```bash
    python main.py
    ```

## Dependencies

- **Python 3.x**
- `python-telegram-bot` library
- `requests` library
- `python-dotenv` for environment variables

## How to Add the Bot to a Chat

1. Find the bot on Telegram via its username: [ByteBuilders Bot](https://t.me/ByteBuilders_bot).
2. Add it to any group chat and grant **admin privileges**.
3. The bot will only respond when users send messages containing the words **"noted"** or **"done"**.

---

**Happy reacting! ❤️**