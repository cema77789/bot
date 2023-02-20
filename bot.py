import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = telegram.Bot(token='5958356665:AAH6qiUNzGkZY-0wwzaF926S7dxToHZ8Y4Y')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт! Я бот, який буде пересилати всі повідомлення, що мені приходять.")

def echo(update, context):
    # Отримати повідомлення, яке було відправлено користувачем
    message = update.message.text
    # Відправити повідомлення користувачу, який запустив бота
    context.bot.send_message(chat_id=<@cema77789>, text=message)

updater = Updater(token='5958356665:AAH6qiUNzGkZY-0wwzaF926S7dxToHZ8Y4Y', use_context=True)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
