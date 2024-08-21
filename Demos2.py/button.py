from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from io import StringIO
from config import token

# Ձեր բոտի API տոքենը
TOKEN = token

# Ֆայլի բովանդակությունը
with open("Բարձր տեխնոլոգիական արդյունաբերություն.txt", 'r', encoding='utf-8') as file:
    file_content = file.read()

# Անսինքրոն start ֆունկցիան
async def start(update: Update, context: CallbackContext) -> None:
    # Ցուցադրեք ողջույնի հաղորդագրությունը
    await update.message.reply_text(
        "Բարի գալուստ! Ես Telegram բոտ եմ, որը կօգնի ձեզ հասկանալու կոռուպցիոն երևույթները հասարակական կյանքում:\n"
        "Օգտագործեք /help հրամանը՝ ավելին իմանալու համար:"
    )

    # Ցուցադրեք մենյուն
    await show_menu(update)

# Անսինքրոն show_menu ֆունկցիան
async def show_menu(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("Բարձր տեխնոլոգիական արդյունաբերություն", callback_data='send_file')],
        # այլ կոճակներ ավելացնել
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Ընտրեք գործողություն:', reply_markup=reply_markup)

# Կոճակների արձագանքը
async def setinline(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'send_file':
        # Ստեղծել ֆայլի նմանակ
        file_stream = StringIO(file_content)
        file_stream.name = 'Բարձր_տեխնոլոգիական_արդյունաբերության_կայք.txt'

        # Ուղարկել ֆայլը
        await context.bot.send_document(chat_id=query.message.chat_id, document=file_stream)
        await query.edit_message_text(text="Ֆայլը ուղարկվեց:")

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
