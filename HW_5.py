import telebot
import random

token = "5968683624:AAFwlTGL1OFkbBzoE-8db2e_g3_j4uq7uqU"
bot = telebot.TeleBot(token)

HELP = """
/help - справка по программе.
/add - добавить задачу.
/show - вывести все задачи.
/exit - выход из программы.
/randTask - добавить случайную задачу.
/randDate - добавить случайную дату.
/random - добавить случайную задачу на случайную дату.

любая иная команда - завершение приложения."""

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Нет задач на указанную Вами дату. (("
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)