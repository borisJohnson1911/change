import telebot
from telebot import types

# git add . && git commit -m "m" && git push heroku master && heroku ps

bot = telebot.TeleBot('647104623:AAETlpH2ZWORYFq7gsZ_zRT3kfJb-v116xI')

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 0 else None

@bot.message_handler(commands=["start"])
def inline(message):
    unique_code = extract_unique_code(message.text)
    if unique_code == "1":
        bot.send_message(message.chat.id, "Продолжение оплаты курса Новичок")
    if unique_code == "2":
        bot.send_message(message.chat.id, "Продолжение оплаты курса Теханализ")
    if unique_code == "3":
        bot.send_message(message.chat.id, "Продолжение оплаты курса Трейдер")
    if unique_code == "4":
        bot.send_message(message.chat.id, "Продолжение оплаты курса Профи")
    if unique_code == "5":
        bot.send_message(message.chat.id, "Продолжение оплаты Торговых сигналов")
    #if unique_code == "":
    #    bot.send_message(message.chat.id, "Старт")    


if __name__ == '__main__':
     bot.polling(none_stop=True)
