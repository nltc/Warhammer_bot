import telebot
from telebot import types
from config import TOKEN, START
from db import select_order, delete_user_order, check_tg_link, check_order, ready_to_order, send_order


bot = telebot.TeleBot(TOKEN)

def main_menu(callback):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    warhammer = types.InlineKeyboardButton(text='Warhammer 40K', callback_data='warhammer_menu')
    terrein = types.InlineKeyboardButton(text='Террейн', callback_data='terrein_menu')
    accesorios = types.InlineKeyboardButton(text='Аксессуары', callback_data='accesorios_menu')
    addons = types.InlineKeyboardButton(text='Дополнительно', callback_data='addons_menu')
    order = types.InlineKeyboardButton(text='Корзина', callback_data='order_menu')
    order_pay = types.InlineKeyboardButton(text='Доставка и оплата', callback_data='order_pay_menu')
    about_us = types.InlineKeyboardButton(text='О нас', callback_data='about_us_menu')
    markup_inline.add(warhammer, terrein, accesorios, addons, order, order_pay, about_us)
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


def order_menu(callback):
    order_inline = types.InlineKeyboardMarkup(row_width=1)
    make_order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='make_order')
    delete_order = types.InlineKeyboardButton(text='Очистить корзину', callback_data='delete_order')
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    x = select_order(callback)
    order_inline.add(make_order,delete_order, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=f'Ваш заказ: {x}', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=order_inline)

def make_order(callback):
    if check_tg_link(callback) and check_order(callback):
        bot.answer_callback_query(callback_query_id=callback.id, text="Заказ создан успешно", show_alert=False)
        ready_to_order(callback)
        send_order(callback)
    elif not check_tg_link(callback):
        bot.answer_callback_query(callback_query_id=callback.id, text="Напишите в чат вашу ссылку на телеграм", show_alert=False)
    elif not check_order(callback):
        bot.answer_callback_query(callback_query_id=callback.id, text="Корзина пуста", show_alert=False)

def delete_order(callback):
    delete_user_order(callback)
    order_menu(callback)


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


def addons_menu(callback):
    addons_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    addons_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Дополнительно', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=addons_inline)
