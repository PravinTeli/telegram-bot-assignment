import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = '7559401125:AAGnGB0q4BlwpqTHzN0WYlW1Fit278MCBtU'

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("📋 About", callback_data='about')],
        [InlineKeyboardButton("❓ Help", callback_data='help')],
        [InlineKeyboardButton("🌟 Fun Facts", callback_data='facts')],
        [InlineKeyboardButton("🎯 Commands", callback_data='commands')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        '👋 Hello World! Welcome to my University Assignment Bot!\n\n'
        'Click the buttons below to explore:',
        reply_markup=reply_markup
    )

async def hello_world(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hello World command"""
    await update.message.reply_text('🌍 Hello World! This is my Telegram bot for university assignment!')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About command"""
    about_text = """
👨‍🎓 **About This Bot**

**Creator:** [PRAVIN TELI - 76914 -Group 54DPH]
**Purpose:** University Assignment - Telegram Bot Development
**Course:** [Internet Technologies]
**University:** [menedżerska akademia nauk stosowanych w warszawie]

This bot was created as part of a programming assignment to demonstrate:
- Bot creation with BotFather
- Basic command handling
- Interactive buttons
- Custom responses

Made with ❤️ using Python and python-telegram-bot library
    """
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """
🆘 **Bot Help & Commands**

**Available Commands:**
- `/start` - Welcome message with menu
- `/hello` - Simple Hello World greeting
- `/about` - Information about this bot and creator
- `/help` - Show this help message
- `/facts` - Get interesting random facts
- `/commands` - List all available commands

**How to Use:**
1. Type any command starting with `/`
2. Or click the interactive buttons in menus
3. Send any text message for a friendly response

**Tips:**
- Commands work in private chats and groups
- Use buttons for easier navigation
- Type anything to get a response!

Need more help? Just send me any message! 😊
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def facts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fun facts command"""
    import random
    
    facts = [
        "🐙 Octopuses have three hearts and blue blood!",
        "🍯 Honey never spoils - archaeologists have found 3000-year-old honey that's still edible!",
        "🌙 A day on Venus is longer than its year!",
        "🐨 Koalas sleep 18-22 hours per day!",
        "🦈 Sharks have been around longer than trees!",
        "🧠 Your brain uses about 20% of your body's total energy!",
        "🐧 Penguins can jump up to 6 feet high!",
        "🌊 The ocean produces over 50% of the world's oxygen!",
        "🕷️ Most spiders are smaller than your fingernail!",
        "⚡ Lightning strikes the Earth about 100 times every second!"
    ]
    
    fact = random.choice(facts)
    await update.message.reply_text(f"🌟 **Fun Fact:**\n\n{fact}")

async def commands_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List all commands"""
    commands_text = """
🎯 **All Available Commands:**

**Basic Commands:**
- `/start` - Start the bot and show main menu
- `/hello` - Hello World greeting

**Information Commands:**
- `/about` - About the bot and creator
- `/help` - Detailed help information
- `/facts` - Random interesting facts
- `/commands` - This commands list

**Interactive Features:**
- Click buttons in menus for easy navigation
- Send any text for a friendly response
- All commands work with `/` prefix

**Example Usage:**
Just type: `/hello` or `/facts`
    """
    await update.message.reply_text(commands_text, parse_mode='Markdown')

# Button callback handler
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses"""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback
    
    if query.data == 'about':
        about_text = """
👨‍🎓 **About This Bot**

**Creator:** [Your Name Here]
**Purpose:** University Assignment
**Made with:** Python & Telegram Bot API

This bot demonstrates:
✅ Command handling
✅ Interactive buttons  
✅ Custom responses
✅ Help system

Click /start to return to main menu
        """
        await query.edit_message_text(about_text, parse_mode='Markdown')
        
    elif query.data == 'help':
        help_text = """
🆘 **Quick Help**

**Commands:** `/start`, `/hello`, `/about`, `/help`, `/facts`

**Usage:** 
- Type commands with `/`
- Click buttons for navigation
- Send any message for response

Click /start to return to main menu
        """
        await query.edit_message_text(help_text, parse_mode='Markdown')
        
    elif query.data == 'facts':
        import random
        facts = [
            "🐙 Octopuses have 3 hearts!",
            "🍯 Honey never expires!",
            "🌙 Venus day > Venus year!",
            "🦈 Sharks predate trees!",
            "🐧 Penguins jump 6 feet high!"
        ]
        fact = random.choice(facts)
        await query.edit_message_text(f"🌟 **Fun Fact:**\n\n{fact}\n\nClick /start for main menu")
        
    elif query.data == 'commands':
        cmd_text = """
🎯 **Commands:**

- `/start` - Main menu
- `/hello` - Hello World  
- `/about` - Bot info
- `/help` - Help guide
- `/facts` - Random facts

Click /start to return to main menu
        """
        await query.edit_message_text(cmd_text, parse_mode='Markdown')

# Handle regular messages (not commands)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle non-command messages"""
    responses = [
        "Thanks for your message! 😊",
        "Hello there! Try using /start to see what I can do!",
        "I'm here to help! Use /help for available commands.",
        "Nice to hear from you! Check out /facts for something interesting!",
        "Hi! I'm a university assignment bot. Try /about to learn more!"
    ]
    
    import random
    response = random.choice(responses)
    await update.message.reply_text(response)

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("hello", hello_world))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("facts", facts_command))
    application.add_handler(CommandHandler("commands", commands_list))
    
    # Add callback handler for buttons
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Add message handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    print("🤖 Bot is starting...")
    print("Press Ctrl+C to stop the bot")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()