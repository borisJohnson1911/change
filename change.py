import telebot, requests, urllib
from telebot import types
from urllib.request import urlopen
from github import Github
from github import InputGitTreeElement
from array import array

# git add . && git commit -m "m" && git push heroku master && heroku ps

bot = telebot.TeleBot('647104623:AAETlpH2ZWORYFq7gsZ_zRT3kfJb-v116xI')

kb1 = types.InlineKeyboardMarkup(row_width=1)
b1 = types.InlineKeyboardButton(text="Оплатить", callback_data="b1")
promo1 = types.InlineKeyboardButton(text="Ввести промокод", callback_data="promo1")
kb1.add(b1, promo1)

kb2 = types.InlineKeyboardMarkup(row_width=1)
b2 = types.InlineKeyboardButton(text="Оплатить", callback_data="b2")
promo2 = types.InlineKeyboardButton(text="Ввести промокод", callback_data="promo2")
kb2.add(b2, promo2)

kb3 = types.InlineKeyboardMarkup(row_width=1)
b3 = types.InlineKeyboardButton(text="Оплатить", callback_data="b3")
promo3 = types.InlineKeyboardButton(text="Ввести промокод", callback_data="promo3")
kb3.add(b3, promo3)

kb4 = types.InlineKeyboardMarkup(row_width=1)
b4 = types.InlineKeyboardButton(text="Оплатить", callback_data="b4")
promo4 = types.InlineKeyboardButton(text="Ввести промокод", callback_data="promo4")
kb4.add(b4, promo4)

kb5 = types.InlineKeyboardMarkup(row_width=1)
b5 = types.InlineKeyboardButton(text="Оплатить", callback_data="b5")
promo5 = types.InlineKeyboardButton(text="Ввести промокод", callback_data="promo5")
kb5.add(b5, promo5)

bp1 = types.InlineKeyboardMarkup(row_width=1)
bp11 = types.InlineKeyboardButton(text="Оплатить", callback_data="bp1")
bp1.add(bp11)

bp2 = types.InlineKeyboardMarkup(row_width=1)
bp22 = types.InlineKeyboardButton(text="Оплатить", callback_data="bp2")
bp2.add(bp22)

bp3 = types.InlineKeyboardMarkup(row_width=1)
bp33 = types.InlineKeyboardButton(text="Оплатить", callback_data="bp3")
bp3.add(bp33)

bp4 = types.InlineKeyboardMarkup(row_width=1)
bp44 = types.InlineKeyboardButton(text="Оплатить", callback_data="bp4")
bp4.add(bp44)

bp5 = types.InlineKeyboardMarkup(row_width=1)
bp55 = types.InlineKeyboardButton(text="Оплатить", callback_data="bp5")
bp5.add(bp55)

bp1p = types.InlineKeyboardMarkup(row_width=1)
bp11p = types.InlineKeyboardButton(text="Оплатить", callback_data="bp1p")
bp1p.add(bp11p)

bp2p = types.InlineKeyboardMarkup(row_width=1)
bp22p = types.InlineKeyboardButton(text="Оплатить", callback_data="bp2p")
bp2p.add(bp22p)

bp3p = types.InlineKeyboardMarkup(row_width=1)
bp33p = types.InlineKeyboardButton(text="Оплатить", callback_data="bp3p")
bp3p.add(bp33p)

bp4p = types.InlineKeyboardMarkup(row_width=1)
bp44p = types.InlineKeyboardButton(text="Оплатить", callback_data="bp4p")
bp4p.add(bp44p)

bp5p = types.InlineKeyboardMarkup(row_width=1)
bp55p = types.InlineKeyboardButton(text="Оплатить", callback_data="bp5p")
bp5p.add(bp55p)

backfp1 = types.InlineKeyboardMarkup(row_width=1)
backfp11 = types.InlineKeyboardButton(text="Назад", callback_data="backfp1")
backfp1.add(backfp11)

backfp2 = types.InlineKeyboardMarkup(row_width=1)
backfp22 = types.InlineKeyboardButton(text="Назад", callback_data="backfp2")
backfp2.add(backfp22)

backfp3 = types.InlineKeyboardMarkup(row_width=1)
backfp33 = types.InlineKeyboardButton(text="Назад", callback_data="backfp3")
backfp3.add(backfp33)

backfp4 = types.InlineKeyboardMarkup(row_width=1)
backfp44 = types.InlineKeyboardButton(text="Назад", callback_data="backfp4")
backfp4.add(backfp44)

backfp5 = types.InlineKeyboardMarkup(row_width=1)
backfp55 = types.InlineKeyboardButton(text="Назад", callback_data="backfp5")
backfp5.add(backfp55)

third = types.InlineKeyboardMarkup(row_width=1)
thirdb = types.InlineKeyboardButton(text="Перейти", url="https://t.me/wetrader_bot?start=1")
third.add(thirdb)

signals = types.InlineKeyboardMarkup(row_width=1)
sig = types.InlineKeyboardButton(text="Перейти", url="https://t.me/wetrader_bot?start=2")
signals.add(sig)

st = types.InlineKeyboardMarkup(row_width=1)
st1 = types.InlineKeyboardButton(text="Оплатить", callback_data="st1")
st.add(st1)

ch = types.InlineKeyboardMarkup(row_width=1)
ch1 = types.InlineKeyboardButton(text="Проверить оплату", callback_data="ch1")
ch.add(ch1)

ip = types.InlineKeyboardMarkup(row_width=1)
ip1 = types.InlineKeyboardButton(text="Я оплатил", callback_data="ip1")
ip.add(ip1)

def extract_unique_code(text):
    if len(text.split()) > 1:
        return text.split()[1]
    else:
        return "6"

@bot.message_handler(commands=["start"])
def inline(message):
    unique_code = extract_unique_code(message.text)
    if unique_code == "1":
        bot.send_message(message.chat.id, text="Продолжение оплаты курса Новичок", reply_markup=kb1)
    if unique_code == "2":
        bot.send_message(message.chat.id, text="Продолжение оплаты курса Теханализ", reply_markup=kb2)
    if unique_code == "3":
        bot.send_message(message.chat.id, text="Продолжение оплаты курса Трейдер", reply_markup=kb3)
    if unique_code == "4":
        bot.send_message(message.chat.id, text="Продолжение оплаты курса Профи", reply_markup=kb4)
    if unique_code == "5":
        bot.send_message(message.chat.id, text="Продолжение оплаты Торговых сигналов", reply_markup=kb5)
    if unique_code == "6":
        bot.send_message(message.chat.id, "Стартовое сообщение", reply_markup=st)    

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'b1':
        b1 = 0
        u1 = c.from_user.username + '\n'
        with open("Novichok.txt") as C1:
            for line in C1:
                if line == u1:
                    b1 = b1+1
                else:
                    b1 = b1+0
        if b1 == 1:
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, "Вы уже оплатили этот курс! Для получения перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
        else:
            U1 = c.from_user.username
            O1 = open("Novichok.txt", "a")
            O1.write(U1)
            O1.write("\n")
            O1.close()
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Novichok.txt']
            file_names = ['Novichok.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            #Commit
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, text="Оплата прошла успешно! Для получения курса перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
    if c.data == 'b2':
        b2 = 0
        u2 = c.from_user.username + '\n'
        with open("Tehanaliz.txt") as C2:
            for line in C2:
                if line == u2:
                    b2 = b2+1
                else:
                    b2 = b2+0
        if b2 == 1:
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, "Вы уже оплатили этот курс! Для получения перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
        else:
            U2 = c.from_user.username
            O2 = open("Tehanaliz.txt", "a")
            O2.write(U2)
            O2.write("\n")
            O2.close()
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Tehanaliz.txt']
            file_names = ['Tehanaliz.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            #Commit
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, text="Оплата прошла успешно! Для получения курса перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
    if c.data == 'b3':
        b3 = 0
        u3 = c.from_user.username + '\n'
        with open("Trader.txt") as C3:
            for line in C3:
                if line == u3:
                    b3 = b3+1
                else:
                    b3 = b3+0
        if b3 == 1:
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, "Вы уже оплатили этот курс! Для получения перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
        else:
            U3 = c.from_user.username
            O3 = open("Trader.txt", "a")
            O3.write(U3)
            O3.write("\n")
            O3.close()
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Trader.txt']
            file_names = ['Trader.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            #Commit
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, text="Оплата прошла успешно! Для получения курса перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
    if c.data == 'b4':
        b4 = 0
        u4 = c.from_user.username + '\n'
        with open("Profi.txt") as C4:
            for line in C4:
                if line == u4:
                    b4 = b4+1
                else:
                    b4 = b4+0
        if b4 == 1:
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, "Вы уже оплатили этот курс! Для получения перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
        else:
            U4 = c.from_user.username
            O4 = open("Profi.txt", "a")
            O4.write(U4)
            O4.write("\n")
            O4.close()
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Profi.txt']
            file_names = ['Profi.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            #Commit
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, text="Оплата прошла успешно! Для получения курса перейдите в бота WeTrade, нажмите START и выберите оплаченный Вами крус!", reply_markup=third)
    if c.data == 'b5':
        b5 = 0
        u5 = c.from_user.username + '\n'
        with open("Signals.txt") as C5:
            for line in C5:
                if line == u5:
                    b5 = b5+1
                else:
                    b5 = b5+0
        if b5 == 1:
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, text="Вы уже оплатили Торговые сигналы! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=signals)
        else:
            U5 = c.from_user.username
            O5 = open("Signals.txt", "a")
            O5.write(U5)
            O5.write("\n")
            O5.close()
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Signals.txt']
            file_names = ['Signals.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            #Commit
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, "Оплата Торговых сигналов прошла успешно! Для получения доступа к Торговым сигналам перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=signals)
    if c.data == 'promo1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Введите промокод")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def promocode(message):
            p1 = open('Promocode.txt', 'r').read()
            if message.text == p2:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен верно", reply_markup=bp1p)
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен неверно", reply_markup=backfp1)
    if c.data == 'promo2':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Введите промокод")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def promocode(message):
            p2 = open('Promocode.txt', 'r').read()
            if message.text == p2:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен верно", reply_markup=bp2p)
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен неверно", reply_markup=backfp2)
    if c.data == 'promo3':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Введите промокод")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def promocode(message):
            p3 = open('Promocode.txt', 'r').read()
            if message.text == p3:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен верно", reply_markup=bp3p)
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен неверно", reply_markup=backfp3)
    if c.data == 'promo4':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Введите промокод")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def promocode(message):
            p4 = open('Promocode.txt', 'r').read()
            if message.text == p4:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен верно", reply_markup=bp4p)
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен неверно", reply_markup=backfp4)
    if c.data == 'promo5':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Введите промокод")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def promocode(message):
            p5 = open('Promocode.txt', 'r').read()
            if message.text == p5:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен верно", reply_markup=bp5p)
            else:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
                bot.send_message(c.message.chat.id, text="Промокод введен неверно", reply_markup=backfp5)
    if c.data == 'bp1':
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=third)
    if c.data == 'bp2':
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=third)
    if c.data == 'bp3':
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=third)
    if c.data == 'bp4':
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=third)
    if c.data == 'bp5':
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу!", reply_markup=signals)
    if c.data == 'bp1p':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу! (промо)", reply_markup=third)
    if c.data == 'bp2p':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу! (промо)", reply_markup=third)
    if c.data == 'bp3p':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу! (промо)", reply_markup=third)
    if c.data == 'bp4p':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу! (промо)", reply_markup=third)
    if c.data == 'bp5p':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, "Оплата прошла успешно! Для получения доступа перейдите в бота WeTrade, нажмите START по кнопке снизу! (промо)", reply_markup=signals)
    if c.data == 'backfp1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Продолжение оплаты курса Новичок", reply_markup=kb1)
    if c.data == 'backfp2':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Продолжение оплаты курса Теханализ", reply_markup=kb2)
    if c.data == 'backfp3':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Продолжение оплаты курса Трейдер", reply_markup=kb3)
    if c.data == 'backfp4':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Продолжение оплаты курса Профи", reply_markup=kb4)
    if c.data == 'backfp5':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Продолжение оплаты Торговых сигналов", reply_markup=kb5)
    if c.data == 'st1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Оплата принимается только в криптовалюте\nСумма оплаты: 0,9999 BTC\nBTC-адресс: 8fvb47399vbskf9vjd09jvsl\nТранзакция обрабатывается в полуавтоматическом режиме, сумма зачисляется после 2-ух подтверждений", reply_markup=ip)
    if c.data == 'ip1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Введите номер транзакции:")
        @bot.message_handler(func=lambda message: True, content_types=['text'])
        def ip11(message):
            ip111 = open('Transaction.txt', 'a')
            ip111.write(message.text)
            #Push to GitHub
            user = "Stuffman"
            password = "Boryan99"
            g = Github(user,password)
            repo = g.get_user().get_repo('change')
            file_list = ['Transaction.txt']
            file_names = ['Transaction.txt']
            commit_message = 'New payment'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        bot.send_message(c.message.chat.id, c.message.message.id, text="Ваш платеж находится в процессе обработки", reply_markup=ch)
    if c.data == 'ch1':
        bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.send_message(c.message.chat.id, text="Ваш платеж находится в процессе обработки", reply_markup=ch)
    
if __name__ == '__main__':
     bot.polling(none_stop=True)

