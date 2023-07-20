import requests
from random import randrange
from bs4 import BeautifulSoup as b
import telebot
from t0ken import *

bot = telebot.TeleBot(TOKEN)

def parse_url(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return ([c.text for c in anekdots])

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем кнопку "Отправить сообщение"
    markup = telebot.types.ReplyKeyboardMarkup()
    item = telebot.types.KeyboardButton('Получить анек')
    markup.add(item)
    bot.send_message(message.chat.id, "Привет! Скину случайный анек, если нажмешь на кнопку", reply_markup=markup)

# Обработчик нажатия кнопки "Отправить сообщение"
@bot.message_handler(func=lambda message: message.text == 'Получить анек')
def send_message(message):
    a = parse_url('https://www.anekdot.ru/random/anekdot/')
    bot.send_message(message.chat.id, a[randrange(21)])

if __name__ == "__main__":
    bot.polling()
