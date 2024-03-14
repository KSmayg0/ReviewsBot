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
    req = call.data.split('_')
    
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
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
    driver.implicitly_wait(10)
    elements = driver.find_element(By.ID, 'app') 
    card_elements = elements.find_elements(By.CLASS_NAME, "product-card__link")
    img_elements = elements.find_elements(By.CLASS_NAME, "j-thumbnail")
    images = []
    titles = []
    links = []
    for image in img_elements:
        image_link = image.get_attribute("src")
        images.append(image_link)
    for product in card_elements:
        product_title = product.get_attribute("aria-label")
        titles.append(product_title)
        product_link = product.get_attribute("href")
        links.append(product_link)
    # print(images)
    # bot.send_message(message.chat.id, '\n'.join(titles))
    # for i in range (0,3):
    #     bot.send_photo(message.chat.id, photo= f'{images[i]}', caption=f'{links[i]}''\n'f'{titles[i]}')
    #     inlinemarkup = types.InlineKeyboardMarkup() 
    #     inlinebutton1 = types.InlineKeyboardButton('<<', callback_data='last page')
    #     inlinebutton2 = types.InlineKeyboardButton('>>', callback_data='next page')
    #     inlinemarkup.row(inlinebutton1, inlinebutton2)
    # buttontext = f'______'
    # markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    # inlinemarkup = types.InlineKeyboardMarkup() 
    # inlinebutton1 = types.InlineKeyboardButton('<<', callback_data='last page')
    # inlinebutton2 = types.InlineKeyboardButton('>>', callback_data='next page')
    # inlinemarkup.row(inlinebutton1, inlinebutton2)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    for i in range (0,3):
        # bot.edit_message_media(message.chat.id, next, buttontext, reply_markup = inlinemarkup)
        bot.send_photo(message.chat.id, photo= f'{images[i]}', caption=f'{links[i]}''\n'f'{titles[i]}',reply_markup=markup)
    # print(titles)
    # print(links)


# ПОМОЩЬ ПОЛЬЗОВАТЕЛЮ
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Основные команды бота:</b>', parse_mode='html')

bot.infinity_polling()