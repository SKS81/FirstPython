# создание бота, отвечающего на сообщения зеркально
# FirstPythonEchoBot
# имя бота @EchoSKS81Bot
# ссылка https://t.me/EchoSKS81Bot
# токен 5906828776:AAFuRGrDmoZ26wXrf2ufxW4taP4hiC4i5uQ

import telebot

token = "5906828776:AAFuRGrDmoZ26wXrf2ufxW4taP4hiC4i5uQ"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, я на связи!')

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)