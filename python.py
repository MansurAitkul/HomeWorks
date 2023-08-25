from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '6531598030:AAFU6_e6kVmZ0XGnmZL7dJHe9IdCaLtDlu0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который будет пересылать вам ваши сообщения.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
