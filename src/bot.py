import os
import time
import telebot

import src.config as cfg
from local_kalik import get_nearest_kalik, GeoData

bot = telebot.TeleBot(cfg.TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btns = telebot.types.InlineKeyboardButton("😈 Показать кальянные 😶‍🌫️", callback_data="show_hookah")
    markup.add(btns)
    bot.send_message(message.chat.id, cfg.HELLO_MESSAGE, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, cfg.HELP_MESSAGE)


@bot.callback_query_handler(lambda query: query.data == "show_hookah")
def menu_actions(query):
    bot.answer_callback_query(query.id)
    bot.send_message(query.message.chat.id, "TODO")


@bot.message_handler(content_types=['location'])
def get_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    p_geo_pos = GeoData(lat=lat, lon=lon)
    bot.send_message(message.chat.id, f'Ближайший калик:\n {get_nearest_kalik(p_geo_pos)}')


if __name__ == "__main__":
    bot.polling(none_stop=True)
