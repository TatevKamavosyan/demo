from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
from config import token
from openai_integration import ask_assistant

TOKEN = token

# Define text files and their paths
text_files = {
    'corruption': 'text_am/Կոռուպցիա․txt',
    'prime_minister': 'text_am/ՀՀ վարչապետը.txt',
    'foreign_affairs': 'text_am/ՀՀ արտաքին գործերի.txt',
    'tech_industry': 'text_am/Բարձր տեխնոլոգիական արդյունաբերություն.txt',
    'social_issues': 'text_am/ՀՀ Աշխատանքի և սոցիալական հարցերի ոլորտում.txt',
    'justice': 'text_am/ՀՀ արդարադատության ոլորտում.txt',
    'education': 'text_am/ՀՀ Կրթության, գիտության, մշակույթի և սպորտի.txt',
    'environment': 'text_am/Շրջակա միջավայրի.txt',
    'local_government': 'text_am/ՀՀ թաղապետարաններում, քաղաքապետարանում.txt',
    'economy': 'text_am/ՀՀ էկոնոմիկայի.txt',
    'internal_affairs': 'text_am/ՀՀ ներքին գործերի.txt',
    'territorial_management': 'text_am/ՀՀ Տարածքային կառավարման և ենթակառուցվածքների.txt',
     'finances':'text_am/ՀՀ ֆինանսների.txt',
     'media':'text_am/ԶԼՄ․txt',
    'party': 'text_am/կուսակցություն․txt',
     'protection':'text_am/ՀՀ պաշտպանության.txt',
     'healthcare': 'text_am/ՀՀ առողջապահության .txt',
     'matenadaran': 'text_am/ՀՀ մատենադարանում, թանգարաններում, ցուցասրահներում և արխիվներում .txt',
     'deputy': 'text_am/պատգամավոր․txt',

}

# Load the content of the text files into memory
texts = {key: open(path, 'r', encoding='utf-8').read() for key, path in text_files.items()}

# For storing message IDs
user_messages = {}

async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await show_menu(chat_id, context)

async def show_menu(chat_id: int, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Կոռուպցիա", callback_data='corruption')],
        [InlineKeyboardButton("ՀՀ Արտաքին գործեր", callback_data='foreign_affairs')],
        [InlineKeyboardButton("Բարձր տեխնոլոգիական արդյունաբերություն", callback_data='tech_industry')],
        [InlineKeyboardButton("ՀՀ Աշխատանքի և սոցիալական հարցեր", callback_data='social_issues')],
        [InlineKeyboardButton("ՀՀ Արդարադատություն", callback_data='justice')],
        [InlineKeyboardButton("ՀՀ կրթության գիտության մշակույթի և սպորտի", callback_data='education')],
        [InlineKeyboardButton("Շրջակա միջավայրի", callback_data='environment')],
        [InlineKeyboardButton("ՀՀ թաղապետարաններում և քաղաքապետարանում", callback_data='local_government')],
        [InlineKeyboardButton("ՀՀ Էկոնոմիկայի", callback_data='economy')],
        [InlineKeyboardButton("ՀՀ ներքին գործերի", callback_data='internal_affairs')],
        [InlineKeyboardButton("ՀՀ Տարածքային կառավարման և ենթակառուցվածքների", callback_data='territorial_management')],
        [InlineKeyboardButton("ՀՀ վարչապետ", callback_data='prime_minister')],
        [InlineKeyboardButton("ԶԼՄ", callback_data='media')],
        [InlineKeyboardButton("Կուսակցություն", callback_data='party')],
        [InlineKeyboardButton("ՀՀ պաշտպանություն", callback_data='protection')],
        [InlineKeyboardButton("ՀՀ առողջապահություն", callback_data='heathcare')],
        [InlineKeyboardButton("Մատենադարան, արխիվ, թանգարան", callback_data='matenadaran')],
        [InlineKeyboardButton("ՀՀ ֆինանսներ", callback_data='finance')],
        [InlineKeyboardButton("Պատգամավոր", callback_data='deputy')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text="Ընտրեք ոլորտը:", reply_markup=reply_markup)

async def show_text(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id
    message_id = query.message.message_id

    # Delete previous messages
    if chat_id in user_messages:
        for msg_id in user_messages[chat_id]:
            if msg_id != message_id:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
                except Exception as e:
                    print(f"Cannot delete message {msg_id}: {e}")
        user_messages[chat_id].clear()

    user_messages.setdefault(chat_id, []).append(message_id)

    if query.data in texts:
        content = texts[query.data]
        new_message = await context.bot.send_message(chat_id=chat_id, text=content)

        keyboard = [[InlineKeyboardButton("Փակել", callback_data='close')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=chat_id, text="Այստեղ է ցուցադրված բովանդակությունը:", reply_markup=reply_markup)

        user_messages[chat_id].append(new_message.message_id)

    elif query.data == 'close':
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        await show_menu(chat_id, context)

async def askme_command(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text="Waiting for your input.")

async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_input = update.message.text

    # Show loading message
    loading_message = await context.bot.send_message(chat_id=chat_id, text="Loading...")

    # Get the AI response
    response = ask_assistant(user_input)

    # Update the message with the AI response
    await context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=loading_message.message_id,
        text=response
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('askme', askme_command))

    # Button handlers
    application.add_handler(CallbackQueryHandler(show_text))

    # Text message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
