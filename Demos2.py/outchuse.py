from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from config import token

# Ձեր բոտի API տոքենը
TOKEN = token

# Ֆայլի բովանդակությունը
with open("Բարձր տեխնոլոգիական արդյունաբերություն.txt", 'r', encoding='utf-8') as file:
    file_content = file.read()


# Անսինքրոն start ֆունկցիան
async def start(update: Update, context: CallbackContext) -> None:
    # Ցուցադրեք մենյուն առանց ողջույնի հաղորդագրության
    await show_menu(update)


# Անսինքրոն show_menu ֆունկցիան
async def show_menu(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Բարձր տեխնոլոգիական արդյունաբերություն", callback_data='send_file')],
        # այլ կոճակներ ավելացնել
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Ստեղծել և ուղարկել դատարկ հաղորդագրություն, որում կոճակներն են
    message = await update.message.reply_text('')  # Ստեղծել նոր հաղորդագրություն
    await update.message.reply_text(text='', reply_markup=reply_markup)


# Կոճակների արձագանքը
async def setinline(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'send_file':
        # Ուղարկել ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content)
        await query.edit_message_text(text="Ֆայլի պարունակությունը ցուցադրվեց:")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Հրամանների կարգավորումը
    application.add_handler(CommandHandler('start', start))

    # Inline կոճակների կարգավորումը
    application.add_handler(CallbackQueryHandler(setinline))

    # Սկսեք polling-ը
    application.run_polling()


if __name__ == '__main__':
    main()
