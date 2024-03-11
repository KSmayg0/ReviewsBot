from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types

# urlWB = 'https://www.wildberries.ru/'
# pageWB=requests.get(urlWB)
# print(pageWB.status_code)
# soupWB = BeautifulSoup(pageWB.text, "html.parser")
# print(soupWB)
bot = telebot.TeleBot('7108645488:AAGIvGuaGP99lhriHhDwq38kzgfuQhXxHHY')

# ВЫБОР СЕРВИСА (НАЧАЛО)
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='WildBerries', callback_data = 'WB')
    btn2 = types.InlineKeyboardButton(text='Ozon', callback_data = 'Oz')
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, 'Выберите сайт, на котором вы хотите посмотреть отзывы о товаре',reply_markup=markup)
# ВЫБОРЫ ПОЛЬЗОВАТЕЛЯ
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'WB':
        url = 'https://www.wildberries.ru/'
        bot.send_message(call.message.chat.id, 'Вы выбрали сервис <b>WildBerries</b>. Введите товар, на который хотите посмотреть отзывы.', parse_mode='html')
    elif call.data == 'Oz':
        url = 'https://www.ozon.ru/'
        bot.send_message(call.message.chat.id, 'Вы выбрали сервис <b>WildBerries</b>. Введите товар, на который хотите посмотреть отзывы.', parse_mode='html')

# ПОМОЩЬ ПОЛЬЗОВАТЕЛЮ
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Основные команды бота:</b>', parse_mode='html')

bot.infinity_polling()