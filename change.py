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

@bot.message_handler(commands=["start"])
def inline(message):
    bot.send_message(message.chat.id, "Текст первого сообщения", reply_markup=key)


if __name__ == '__main__':
     bot.polling(none_stop=True)
