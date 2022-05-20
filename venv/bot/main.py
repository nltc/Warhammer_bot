import telebot
from telebot import types
from config import TOKEN, START
from Kosmo_desant import *
from Imperium import *
from Chaos import *
from Ksenos import *
from Main_menu import *
from send_email_message import send_email
import re

bot = telebot.TeleBot(TOKEN)

pattern = re.compile('[А-Яа-я]+\s+[А-Яа-я]+\s+[А-Яа-я]+,\s*([0-9])+,\s*(http|https):\/\/t.me\/(([^_])([A-Za-z]{4,32})([^_]))')

@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    warhammer = types.InlineKeyboardButton(text='Warhammer 40K', callback_data='warhammer_menu')
    terrein = types.InlineKeyboardButton(text='Террейн', callback_data='terrein_menu')
    accesorios = types.InlineKeyboardButton(text='Аксессуары', callback_data='accesorios_menu')
    order_pay = types.InlineKeyboardButton(text='Доставка и оплата', callback_data='order_pay_menu')
    about_us = types.InlineKeyboardButton(text='О нас', callback_data='about_us_menu')
    markup_inline.add(warhammer, terrein, accesorios, order_pay, about_us)
    bot.send_photo(message.chat.id, photo=open('pictures/start.png', 'rb'), caption='Самое начало', reply_markup=markup_inline)


@bot.message_handler(content_types=["text"])
def user_order(message):
    if pattern.match(message.text) is not None:
        send_email(message.text)
        bot.send_message(message.chat.id, 'Заказ создан успешно')
        start(message=message)

    else:
        bot.send_message(message.chat.id, 'Введите данные корректно')


@bot.callback_query_handler(func = lambda callback: True)
def main(callback):
    bot.answer_callback_query(callback.id)

    if callback.data == 'warhammer_menu':
        warhammer_menu(callback)

    elif callback.data == 'terrein_menu':
        terrein_menu(callback)

    elif callback.data == 'accesorios_menu':
        accesorios_menu(callback)

    elif callback.data == 'order_pay_menu':
        order_pay_menu(callback)

    elif callback.data == 'about_us_menu':
        about_us_menu(callback)

    elif callback.data == 'main_menu':
        main_menu(callback)

    elif callback.data == 'kosmo_main':
        kosmo_main(callback)

    elif callback.data == 'kosmo_units':
        kosmo_units(callback)

    elif callback.data == 'kosmo_units_technics':
        kosmo_units_technics(callback)

    elif callback.data == 'kosmo_squads':
        kosmo_squads(callback)

    elif callback.data == 'kosmo_characters':
        kosmo_characters(callback)

    elif callback.data == 'orden_kosmo':
        orden_kosmo(callback)

    elif callback.data == 'orden_characters':
        orden_characters(callback)

    elif callback.data == 'orden_technics':
        orden_technics(callback)

    elif callback.data == 'orden_squads':
        orden_squads(callback)

    elif callback.data == 'orden_upgrade':
        orden_upgrade(callback)

    elif callback.data == 'imperium_main':
        imperium_main(callback)

    elif callback.data == 'sororitas_main':
        sororitas_main(callback)

    elif callback.data == 'sororitas_technics':
        sororitas_technics(callback)

    elif callback.data == 'sororitas_squads':
        sororitas_squads(callback)

    elif callback.data == 'sororitas_characters':
        sororitas_characters(callback)

    elif callback.data == 'kustodes_main':
        kustodes_main(callback)

    elif callback.data == 'kustodes_technics':
        kustodes_technics(callback)

    elif callback.data == 'kustodes_squads':
        kustodes_squads(callback)

    elif callback.data == 'kustodes_characters':
        kustodes_characters(callback)

    elif callback.data == 'mechanikus_main':
        mechanikus_main(callback)

    elif callback.data == 'mechanikus_technics':
        mechanikus_technics(callback)

    elif callback.data == 'mechanikus_squads':
        mechanikus_squads(callback)

    elif callback.data == 'mechanikus_characters':
        mechanikus_characters(callback)

    elif callback.data == 'militarium_main':
        militarium_main(callback)

    elif callback.data == 'militarium_technics':
        militarium_technics(callback)

    elif callback.data == 'militarium_squads':
        militarium_squads(callback)

    elif callback.data == 'militarium_characters':
        militarium_characters(callback)

    elif callback.data == 'knigts_main':
        knigts_main(callback)

    elif callback.data == 'inquisition_main':
        inquisition_main(callback)

    elif callback.data == 'chaos_main':
        chaos_main(callback)

    elif callback.data == 'demons_main':
        demons_main(callback)

    elif callback.data == 'demons_squads':
        demons_squads(callback)

    elif callback.data == 'demons_characters':
        demons_characters(callback)

    elif callback.data == 'knights_chaos_main':
        knights_chaos_main(callback)

    elif callback.data == 'kosmo_chaos_main':
        kosmo_chaos_main(callback)

    elif callback.data == 'kosmo_chaos_technics':
        kosmo_chaos_technics(callback)

    elif callback.data == 'kosmo_chaos_squads':
        kosmo_chaos_squads(callback)

    elif callback.data == 'kosmo_chaos_characters':
        kosmo_chaos_characters(callback)

    elif callback.data == 'guard_death_main':
        guard_death_main(callback)

    elif callback.data == 'guard_death_technics':
        guard_death_technics(callback)

    elif callback.data == 'guard_death_squads':
        guard_death_squads(callback)

    elif callback.data == 'guard_death_characters':
        guard_death_characters(callback)

    elif callback.data == 'thousand_sons_main':
        thousand_sons_main(callback)

    elif callback.data == 'thousand_sons_technics':
        thousand_sons_technics(callback)

    elif callback.data == 'thousand_sons_squads':
        thousand_sons_squads(callback)

    elif callback.data == 'ksenos_main':
        ksenos_main(callback)

    elif callback.data == 'aeldari_main':
        aeldari_main(callback)

    elif callback.data == 'aeldari_technics':
        aeldari_technics(callback)

    elif callback.data == 'aeldari_squads':
        aeldari_squads(callback)

    elif callback.data == 'aeldari_characters':
        aeldari_characters(callback)

    elif callback.data == 'drukhari_main':
        drukhari_main(callback)

    elif callback.data == 'drukhari_technics':
        drukhari_technics(callback)

    elif callback.data == 'drukhari_squads':
        drukhari_squads(callback)

    elif callback.data == 'drukhari_characters':
        drukhari_characters(callback)

    elif callback.data == 'genokradi_main':
        genokradi_main(callback)

    elif callback.data == 'genokradi_technics':
        genokradi_technics(callback)

    elif callback.data == 'genokradi_squads':
        genokradi_squads(callback)

    elif callback.data == 'genokradi_characters':
        genokradi_characters(callback)

    elif callback.data == 'necroni_main':
        necroni_main(callback)

    elif callback.data == 'necroni_technics':
        necroni_technics(callback)

    elif callback.data == 'necroni_squads':
        necroni_squads(callback)

    elif callback.data == 'necroni_characters':
        necroni_characters(callback)

    elif callback.data == 'orks_main':
        orks_main(callback)

    elif callback.data == 'orks_technics':
        orks_technics(callback)

    elif callback.data == 'orks_squads':
        orks_squads(callback)

    elif callback.data == 'orks_characters':
        orks_characters(callback)

    elif callback.data == 'tau_main':
        tau_main(callback)

    elif callback.data == 'tau_technics':
        tau_technics(callback)

    elif callback.data == 'tau_squads':
        tau_squads(callback)

    elif callback.data == 'tau_characters':
        tau_characters(callback)

    elif callback.data == 'tiranidi_main':
        tiranidi_main(callback)

    elif callback.data == 'tiranidi_squads':
        tiranidi_squads(callback)

    elif callback.data == 'tiranidi_bugs':
        tiranidi_bugs(callback)












bot.infinity_polling()
# bot.polling(none_stop=True, interval=0)