from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from config import token

# Ձեր բոտի API տոքենը
TOKEN = token

# Ֆայլի բովանդակությունները
with open("ՀՀ բարձր տեխնոլոգիական արդյունաբերություն.txt", 'r', encoding='utf-8') as file:
    file_content_tech = file.read()

with open("ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտ․txt", 'r', encoding='utf-8') as file:
    file_content_labor = file.read()


with open("ՀՀ մատենադարանում, թանգարաններում, ցուցասրահներում և արխիվներում․txt", 'r', encoding='utf-8') as file:
    file_content_labor = file.read()


with open("ՀՀ շրջակա միջավայրի ոլորտում.txt", 'r', encoding='utf-8') as file:
    file_content_labor = file.read()

with open("ՀՀ Վարչապետը․txt", 'r', encoding='utf-8') as file:
    file_content_labor = file.read()

with open("ՀՀ  արդարադատության ոլորտ․txt", 'r', encoding='utf-8') as file:
    file_content_labor = file.read()
# Անսինքրոն start ֆունկցիան
async def start(update: Update, context: CallbackContext) -> None:
    # Ցուցադրեք մենյուն առանց ողջույնի հաղորդագրության
    await show_menu(update)

# Անսինքրոն show_menu ֆունկցիան
async def show_menu(update: Update) -> None:
    keyboard = [
        [InlineKeyboardButton("ՀՀ բարձր տեխնոլոգիական արդյունաբերություն", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտ", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ կրթության, գիտության, մշակույթի և սպորտի", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ մատենադարանում, թանգարաններում, ցուցասրահներում և արխիվներում", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ շրջակա միջավայրի ոլորտում", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ Վարչապետը", callback_data='send_file_tech')],
        [InlineKeyboardButton("ՀՀ  արդարադատության ոլորտ", callback_data='send_file_tech')]

        # այլ կոճակներ ավելացնել
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Ընտրեք գործողություն:', reply_markup=reply_markup)

# Կոճակների արձագանքը
async def setinline(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'send_file_tech':
        # Ուղարկել առաջին ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_tech)
        await query.edit_message_text(text="Բարձր տեխնոլոգիական արդյունաբերության ֆայլի պարունակությունը ցուցադրվեց:")

    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        await query.edit_message_text(text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")


    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        #await query.edit_message_text(text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")


    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        #await query.edit_message_text(
            text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")

    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        #await query.edit_message_text(
            text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")

    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        await query.edit_message_text(
            text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")



    elif query.data == 'send_file_labor':
        # Ուղարկել երկրորդ ֆայլի բովանդակությունը որպես հաղորդագրություն
        await context.bot.send_message(chat_id=query.message.chat_id, text=file_content_labor)
        await query.edit_message_text(
            text="ՀՀ աշխատանքի և սոցիալական հարցերի ոլորտի ֆայլի պարունակությունը ցուցադրվեց:")


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
