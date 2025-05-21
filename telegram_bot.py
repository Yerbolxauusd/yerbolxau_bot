import telebot
import requests

BOT_TOKEN = "7867075333:AAGQaq2Qiw_EJKvvw-D0OwmSHllL6HcUxXs"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот Yerbolxau для ETH/BTC и XAU/USD. Пиши /signal чтобы получить сигнал.")

@bot.message_handler(commands=['signal'])
def signal(message):
    try:
        bot.send_message(message.chat.id, "Сигнал: Покупать ETH!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

def start_bot():
    bot.polling(none_stop=True)
