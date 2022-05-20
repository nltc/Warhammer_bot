import telebot
from telebot import types
from config import TOKEN, START

bot = telebot.TeleBot(TOKEN)

def main_menu(callback):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    warhammer = types.InlineKeyboardButton(text='Warhammer 40K', callback_data='warhammer_menu')
    terrein = types.InlineKeyboardButton(text='Террейн', callback_data='terrein_menu')
    accesorios = types.InlineKeyboardButton(text='Аксессуары', callback_data='accesorios_menu')
    order_pay = types.InlineKeyboardButton(text='Доставка и оплата', callback_data='order_pay_menu')
    about_us = types.InlineKeyboardButton(text='О нас', callback_data='about_us_menu')
    markup_inline.add(warhammer, terrein, accesorios, order_pay, about_us)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Самое начало', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=markup_inline)

def warhammer_menu(callback):
    warhammer_inline = types.InlineKeyboardMarkup(row_width=1)
    desant = types.InlineKeyboardButton(text='Космодесант', callback_data='kosmo_main')
    imp = types.InlineKeyboardButton(text='Силы Империума', callback_data='imperium_main')
    chaos = types.InlineKeyboardButton(text='Армии хаоса', callback_data='chaos_main')
    ksenos = types.InlineKeyboardButton(text='Армии ксеносов', callback_data='ksenos_main')
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    warhammer_inline.add(desant, imp, chaos, ksenos, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=START, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=warhammer_inline)


def terrein_menu(callback):
    terrein_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    terrein_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='террейн', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=terrein_inline)


def accesorios_menu(callback):
    accesorios_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    accesorios_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Аксессуары', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=accesorios_inline)


def order_pay_menu(callback):
    order_pay_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    order_pay_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Доставка и оплата', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=order_pay_inline)


def about_us_menu(callback):
    about_us_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    about_us_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='О нас', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=about_us_inline)