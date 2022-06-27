import telebot
from telebot import types
from config import TOKEN
from Kosmo_desant import *
from Imperium import *
from Chaos import *
from Ksenos import *
from Main_menu import *
from text import Start
from check_number import number_check
from db import add_to_db, delete_user, add_tg_link, add_vk_link, add_email, add_phone_number
import re


bot = telebot.TeleBot(TOKEN)


tg_pattern = re.compile('(http|https):\/\/t.me\/(([^_])([A-Za-z]{4,32})([^_]))')
# vk_pattern = re.compile('(http|https):\/\/vk.com\/(([^_])([A-Za-z]{4,32})([^_]))')
vk_pattern = re.compile('@(([^_])([A-Za-z]{4,32})([^_]))')
email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@bot.message_handler(commands=['start'])
def start(message):
    delete_user(message)
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    warhammer = types.InlineKeyboardButton(text='Warhammer 40K', callback_data='warhammer_menu')
    terrein = types.InlineKeyboardButton(text='Террейн', callback_data='terrein_menu')
    accesorios = types.InlineKeyboardButton(text='Аксессуары', callback_data='accesorios_menu')
    addons = types.InlineKeyboardButton(text='Дополнительно', callback_data='addons_menu')
    order = types.InlineKeyboardButton(text='Корзина', callback_data='order_menu')
    order_pay = types.InlineKeyboardButton(text='Доставка и оплата', callback_data='order_pay_menu')
    about_us = types.InlineKeyboardButton(text='О нас', callback_data='about_us_menu')
    markup_inline.add(warhammer, terrein, accesorios, addons, order, order_pay, about_us)
    bot.send_photo(message.chat.id, photo=open('pictures/start.png', 'rb'), caption=Start, reply_markup=markup_inline)
    add_to_db(message)


@bot.message_handler(content_types=["text"])
def user_order(message):

    '''Проверка валидности номера телефона, подходит ли текст пользователя шаблонам телеграм, вк или почты'''

    if tg_pattern.match(message.text) is not None:
        add_tg_link(message)

    elif vk_pattern.match(message.text) is not None:
        add_vk_link(message)

    elif number_check(message.text):
        add_phone_number(message)

    elif 'vk.com' in message.text:
        add_vk_link(message)

    elif email_pattern.match(message.text) is not None:
        add_email(message)

    else:
        bot.send_message(message.chat.id, 'Введите данные корректно')
        bot.register_next_step_handler(message, user_order)


@bot.callback_query_handler(func = lambda callback: callback.data)
def main(callback):

    inline_callback = {
        'warhammer_menu': warhammer_menu,
        'terrein_menu': terrein_menu,
        'accesorios_menu': accesorios_menu,
        'order_pay_menu': order_pay_menu,
        'addons_menu': addons_menu,
        'order_menu': order_menu,
        'delete_order': delete_order,
        'make_order': make_order,
        'about_us_menu': about_us_menu,
        'main_menu': main_menu,
        'kosmo_main': kosmo_main,
        'kosmo_units': kosmo_units,
        'kosmo_units_technics': kosmo_units_technics,
        'kosmo_squads': kosmo_squads,
        'kosmo_characters': kosmo_characters,
        'orden_kosmo': orden_kosmo,
        'orden_characters': orden_characters,
        'orden_technics': orden_technics,
        'orden_squads': orden_squads,
        'orden_upgrade': orden_upgrade,
        'imperium_main': imperium_main,
        'sororitas_main': sororitas_main,
        'sororitas_technics': sororitas_technics,
        'sororitas_squads': sororitas_squads,
        'sororitas_characters': sororitas_characters,
        'kustodes_main': kustodes_main,
        'kustodes_technics': kustodes_technics,
        'kustodes_squads': kustodes_squads,
        'kustodes_characters': kustodes_characters,
        'mechanikus_main': mechanikus_main,
        'mechanikus_technics': mechanikus_technics,
        'mechanikus_squads': mechanikus_squads,
        'mechanikus_characters': mechanikus_characters,
        'militarium_main': militarium_main,
        'militarium_technics': militarium_technics,
        'militarium_squads': militarium_squads,
        'militarium_characters': militarium_characters,
        'militarium_upgrade': militarium_upgrade,
        'knigts_main': knigts_main,
        'knigts_15001': knigts_15001,
        'add_15001': add_15001,
        'knigts_15002': knigts_15002,
        'add_15002': add_15002,
        'knigts_15003': knigts_15003,
        'add_15003': add_15003,
        'knigts_15004': knigts_15004,
        'add_15004': add_15004,
        'knigts_15005': knigts_15005,
        'add_15005': add_15005,
        'knigts_15006': knigts_15006,
        'add_15006': add_15006,
        'knigts_15007': knigts_15007,
        'add_15007': add_15007,
        'knigts_15008': knigts_15008,
        'add_15008': add_15008,
        'knigts_15009': knigts_15009,
        'add_15009': add_15009,
        'knigts_15010': knigts_15010,
        'add_15010': add_15010,
        'knigts_15011': knigts_15011,
        'add_15011': add_15011,
        'inquisition_main': inquisition_main,
        'chaos_main': chaos_main,
        'upgrade_main': upgrade_main,
        'demons_main': demons_main,
        'demons_squads': demons_squads,
        'demons_characters': demons_characters,
        'knights_chaos_main': knights_chaos_main,
        'knights_chaos_22001': knights_chaos_22001,
        'add_22001': add_22001,
        'knights_chaos_22002': knights_chaos_22002,
        'add_22002': add_22002,
        'knights_chaos_22003': knights_chaos_22003,
        'add_22003': add_22003,
        'knights_chaos_22004': knights_chaos_22004,
        'add_22004': add_22004,
        'knights_chaos_22005': knights_chaos_22005,
        'add_22005': add_22005,
        'knights_chaos_22006': knights_chaos_22006,
        'add_22006': add_22006,
        'knights_chaos_22007': knights_chaos_22007,
        'add_22007': add_22007,
        'kosmo_chaos_main': kosmo_chaos_main,
        'kosmo_chaos_technics': kosmo_chaos_technics,
        'kosmo_chaos_squads': kosmo_chaos_squads,
        'kosmo_chaos_characters': kosmo_chaos_characters,
        'guard_death_main': guard_death_main,
        'guard_death_technics': guard_death_technics,
        'guard_death_squads': guard_death_squads,
        'guard_death_characters': guard_death_characters,
        'thousand_sons_main': thousand_sons_main,
        'thousand_sons_technics': thousand_sons_technics,
        'thousand_sons_characters': thousand_sons_characters,
        'thousand_sons_squads': thousand_sons_squads,
        'ksenos_main': ksenos_main,
        'aeldari_main': aeldari_main,
        'aeldari_technics': aeldari_technics,
        'aeldari_squads': aeldari_squads,
        'aeldari_characters': aeldari_characters,
        'drukhari_main': drukhari_main,
        'drukhari_technics': drukhari_technics,
        'drukhari_squads': drukhari_squads,
        'drukhari_characters': drukhari_characters,
        'genokradi_main': genokradi_main,
        'genokradi_technics': genokradi_technics,
        'genokradi_squads': genokradi_squads,
        'genokradi_characters': genokradi_characters,
        'necroni_main': necroni_main,
        'necroni_technics': necroni_technics,
        'necroni_squads': necroni_squads,
        'necroni_characters': necroni_characters,
        'orks_main': orks_main,
        'orks_technics': orks_technics,
        'orks_squads': orks_squads,
        'orks_characters': orks_characters,
        'tau_main': tau_main,
        'tau_technics': tau_technics,
        'tau_squads': tau_squads,
        'tau_characters': tau_characters,
        'tiranidi_main': tiranidi_main,
        'tiranidi_squads': tiranidi_squads,
        'tiranidi_monstrs': tiranidi_monstrs
    }

    try:
        inline_callback[callback.data](callback)
    except Exception as e:
        print(e)



bot.infinity_polling()
