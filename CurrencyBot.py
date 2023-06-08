import telebot
from BOT.Extentions import *



bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help'])
def help(message:telebot.types.Message):
    text="Чтобы начать работу введите команду боту в следующем формате <имя валюты, цену которой Вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты> через один пробел"
    bot.reply_to(message, text)
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        user_text = message.text.split(' ')
        if len(user_text)!=3:
            raise APIException("Необходимо ввести 3 параметра")
        quote, base, amount = user_text
        result = CurrencyConverter.get_price(quote, base, amount)
    except APIException as a:
        bot.reply_to(message, f"Ошибка в команде:\n{a}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, f"Цена {amount} {keys[quote]} в {keys[base]} составляет {result}")

bot.polling()
