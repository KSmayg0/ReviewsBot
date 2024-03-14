# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
import requests
import telebot
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        bot.send_message(call.message.chat.id, 'Вы выбрали сервис <b>WildBerries</b>. Введите название товара, на который вы хотите посмотреть отзывы.', parse_mode='html')
    elif call.data == 'Oz':
        url = 'https://www.ozon.ru/'
        bot.send_message(call.message.chat.id, 'Вы выбрали сервис <b>WildBerries</b>. Введите название товара, на который вы хотите посмотреть отзывы.', parse_mode='html')
   

# ФУНКЦИИ ДЛЯ ВВЕДЁННОГО ТЕКСТА
@bot.message_handler(content_types=['text'])
def search_product(message):
    url = f'https://www.wildberries.ru/catalog/0/search.aspx?search={message.text}'
    driver = webdriver.Edge(executable_path='D:\edgedriver\msedgedriver.exe')
    driver.get(url)
    driver.implicitly_wait(30)
    elements = driver.find_element(By.ID, 'app') 
    card_elements = elements.find_elements(By.CLASS_NAME, "product-card__link")
    titles = []
    links = []

    for product in card_elements:
        product_title = product.get_attribute("product-card__name")
        titles.append(product_title)
        product_link = product.get_attribute("href")
        links.append(product_link)
    
    # print(links)


# ПОМОЩЬ ПОЛЬЗОВАТЕЛЮ
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Основные команды бота:</b>', parse_mode='html')

bot.infinity_polling()