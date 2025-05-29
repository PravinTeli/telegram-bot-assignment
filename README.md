# Telegram Bot for Assignment 3

## Overview
This repository contains a Telegram chatbot developed as part of the Internet Technologies course at Menedżerska Akademia Nauk Stosowanych w Warszawie. The bot, `@myuniquebot_bot`, demonstrates basic bot creation, command handling, interactive buttons, and custom responses.

## Creator
- **Name**: Pravin Teli (76914 - Group 54DPH)
- **University**: Menedżerska Akademia Nauk Stosowanych w Warszawie
- **Course**: Internet Technologies
- **Purpose**: University Assignment - Telegram Bot Development

## Features
- Greet users with "Hello world" using `/start` or `/hello`.
- Provide information about the bot and creator with `/about`.
- List available commands with `/help`.
- Share random interesting facts with `/fact`.
- Offer interactive buttons (About, Fact, Help) with `/buttons`.

## Prerequisites
- **Python**: Version 3.11 or higher
- **Git**: For cloning the repository
- **Telegram Account**: To interact with the bot

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/PravinTeli/telegram-bot-assignment/tree/main
cd telegram-bot-assignment

2. Create a Virtual Environment
Set up a virtual environment to manage dependencies:
python -m venv .venv
.venv\Scripts\activate

3. Install Dependencies
Install the required Python packages:
pip install python-telegram-bot==20.7 python-dotenv

4. Configure the Bot
Create a .env file in the project directory:
TELEGRAM_BOT_TOKEN=your_bot_token_here

5. Run the Bot
Start the bot using the following command:
python telegram_bot.py

You should see Bot is running... in the terminal. Press Ctrl+C to stop the bot.

Usage
Open Telegram and search for @myuniquebot_bot.
Use the following commands:
/start or /hello: Get a greeting message.
/about: View creator and bot details.
/help: See available commands.
/fact: Receive a random fact.
/buttons: Interact with inline buttons for About, Fact, and Help.
Testing
Verify all commands and button interactions work as expected.
Check the terminal for logs to debug any issues.
Project Structure
telegram_bot.py: Main bot script with command handlers.
.env: Stores the bot token (not included in this repository for security).
.gitignore: Excludes virtual environment and sensitive files.
README.md: This file.
Dependencies
python-telegram-bot==20.7: Telegram bot framework.
python-dotenv: Manages environment variables.
Contributing
This project is for educational purposes. Contributions are welcome for enhancements (e.g., adding more commands or features). Please fork the repository and submit a pull request.

License
This project is licensed under the LGPLv3, as per the python-telegram-bot library requirements.

Acknowledgments
Inspired by the Telegram Bot API documentation: core.telegram.org/bots
Built with guidance from python-telegram-bot docs
Thanks to Professor Dmitriy Kostiuk for the assignment.
Screenshots
Below is a sample output of the /about command:
