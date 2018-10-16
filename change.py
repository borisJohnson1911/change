import telebot
from telebot import types

# git add . && git commit -m "m" && git push heroku master && heroku ps

bot = telebot.TeleBot('647104623:AAETlpH2ZWORYFq7gsZ_zRT3kfJb-v116xI')

#Стартовая клавиатура
key = types.InlineKeyboardMarkup(row_width=1)
but_1 = types.InlineKeyboardButton(text="Обучающие курсы", callback_data="Обучающие курсы")
but_2 = types.InlineKeyboardButton(text="Торговые сигналы", callback_data="Торговые сигналы")
but_3 = types.InlineKeyboardButton(text="Наши специалисты", callback_data="Наши специалисты")
but_4 = types.InlineKeyboardButton(text="Задать вопрос", callback_data="Задать вопрос")
key.add(but_1, but_2, but_3, but_4)

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

def in_storage(unique_code):
    return True

@bot.message_handler(commands=["start"])
def inline1(message):
    unique_code = extract_unique_code(message.text)
    if unique_code:
        if unique_code==1:
            bot.send_message(message.chat.id, "First is done")

@bot.message_handler(commands=["start 1"])
def inline1(message):
    bot.send_message(message.chat.id, "First is done")
	
@bot.message_handler(commands=["start2"])
def inline2(message):
    bot.send_message(message.chat.id, "Second is done")


if __name__ == '__main__':
     bot.polling(none_stop=True)
