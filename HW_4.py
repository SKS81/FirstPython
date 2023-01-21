import telebot

token = "5906828776:AAFuRGrDmoZ26wXrf2ufxW4taP4hiC4i5uQ"

bot = telebot.TeleBot(token)

name = 'Саша'

@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Привет, я на связи! Я - бот-зеркальщик, я буду отвечать Вам Вашими же сообщениями)))')

@bot.message_handler(content_types=["text"])
def echo(message):

    if name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True, interval=0)