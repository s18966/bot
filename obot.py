import telebot
import re
import datetime

token = "1344299453:AAGShVatEnJ8vhGZymhUlh7bCqVfFRCjxRc";

bot = telebot.TeleBot(token);

@bot.message_handler(content_types=['text'])
def delete_msg(message):
    msg = message.text
    print(msg)
    print(message)

    date = datetime.datetime.today()
    timestamp = date.timestamp()
    print(timestamp)
    result = re.search(r'[oøOоОó‎‎Ó‎öôœо○ºŒ0∆]', msg)
    print(timestamp - message.date)

    if result != None and timestamp - message.date <5:
        #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        print(message)
        bot.send_message(message.chat.id, 'У нас такие буквы запрещены >:c', reply_to_message_id=message.message_id)
bot.polling()