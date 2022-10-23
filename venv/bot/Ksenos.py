import telebot
from text import Ksenos, Aeldari, Aeldari_Technics, Aeldari_Squads, Aeldari_Characters, Drukhari, Drukhari_Technics, \
Drukhari_Squads, Drukhari_Characters, Genokradi, Genokradi_Technics, Genokradi_Squads, Genokradi_Characters, Necroni, \
Necroni_Technics, Necroni_Squads, Necroni_Characters, Orks, Orks_Technics, Orks_Squads, Orks_Characters, Tau, \
Tau_Technics, Tau_Squads, Tau_Characters, Tiranidi, Tiranidi_Squads, Tiranidi_Monstrs
from telebot import types
from config import TOKEN
from db import add_to_order


bot = telebot.TeleBot(TOKEN)


def ksenos_main(callback):
    '''Меню Ксеносов'''

    ksenos_inline = types.InlineKeyboardMarkup(row_width=1)
    aeldari = types.InlineKeyboardButton(text='Аэльдари', callback_data='aeldari_main')
    drukhari = types.InlineKeyboardButton(text='Друкхари', callback_data='drukhari_main')
    genokradi = types.InlineKeyboardButton(text='Культ генокрадов', callback_data='genokradi_main')
    necroni = types.InlineKeyboardButton(text='Некроны', callback_data='necroni_main')
    orks = types.InlineKeyboardButton(text='Орки', callback_data='orks_main')
    tau = types.InlineKeyboardButton(text='Империя Тау', callback_data='tau_main')
    tiranidi = types.InlineKeyboardButton(text='Тираниды', callback_data='tiranidi_main')
    menu = types.InlineKeyboardButton(text='Назад ', callback_data='warhammer_menu')
    ksenos_inline.add(aeldari, drukhari, genokradi, necroni, orks, tau, tiranidi, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/main.jpg', 'rb'), caption=Ksenos, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=ksenos_inline)


def aeldari_main(callback):
    '''Меню Аэльдари'''

    aeldari_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='aeldari_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='aeldari_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='aeldari_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    aeldari_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Аэльдари/main.png', 'rb'), caption=Aeldari, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_inline)


def aeldari_technics(callback):
    '''Техника Аэльдари'''

    aeldari_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Аэльдари/Техника/main.jpg', 'rb'), caption=Aeldari_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_technics_inline)


def aeldari_squads(callback):
    '''Отряды Аэльдари'''

    aeldari_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Аэльдари/Отряды/main.jpg', 'rb'), caption=Aeldari_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_squads_inline)


def aeldari_characters(callback):
    '''Персонажи Аэльдари'''

    aeldari_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Аэльдари/Персонажи/main.jpg', 'rb'), caption=Aeldari_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_characters_inline)


def drukhari_main(callback):
    '''Меню Друкхари'''

    drukhari_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='drukhari_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='drukhari_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='drukhari_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    drukhari_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Друкхари/main.jpg', 'rb'), caption=Drukhari, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_inline)


def drukhari_technics(callback):
    '''Техника Друкхари'''

    drukhari_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Друкхари/Техника/main.jpg', 'rb'), caption=Drukhari_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_technics_inline)


def drukhari_squads(callback):
    '''Отряды Друкхари'''

    drukhari_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Друкхари/Отряды/main.jpg', 'rb'), caption=Drukhari_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_squads_inline)


def drukhari_characters(callback):
    '''Персонажи Друкхари'''

    drukhari_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Друкхари/Персонажи/main.jpg', 'rb'), caption=Drukhari_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_characters_inline)


def genokradi_main(callback):
    '''Меню Культа Генокрадов'''

    genokradi_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='genokradi_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='genokradi_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='genokradi_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    genokradi_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Культ генокрадов/main.jpg', 'rb'), caption=Genokradi, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_inline)


def genokradi_technics(callback):
    '''Техника Культа Генокрадов'''

    genokradi_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Культ генокрадов/Техника/main.jpg', 'rb'), caption=Genokradi_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_technics_inline)


def genokradi_squads(callback):
    '''Отряды Культа Генокрадов'''

    genokradi_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Культ генокрадов/Отряды/main.jpg', 'rb'), caption=Genokradi_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_squads_inline)


def genokradi_characters(callback):
    '''Персонажи Культа Генокрадов'''

    genokradi_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Культ генокрадов/Персонажи/main.jpg', 'rb'), caption=Genokradi_Characters , type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_characters_inline)


def necroni_main(callback):
    '''Меню Некронов'''

    necroni_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='necroni_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='necroni_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='necroni_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    necroni_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Некроны/main.jpg', 'rb'), caption=Necroni, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_inline)


def necroni_technics(callback):
    '''Техника Некронов'''

    necroni_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Некроны/Техника/main.jpg', 'rb'), caption=Necroni_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_technics_inline)


def necroni_squads(callback):
    '''Отряды Некронов'''

    necroni_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Некроны/Отряды/main.jpg', 'rb'), caption=Necroni_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_squads_inline)


def necroni_characters(callback):
    '''Персонажи Некронов'''

    necroni_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Некроны/Персонажи/main.jpg', 'rb'), caption=Necroni_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_characters_inline)


def orks_main(callback):
    '''Меню Орков'''

    orks_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='orks_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='orks_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='orks_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    orks_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Орки/main.jpg', 'rb'), caption=Orks, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_inline)


def orks_technics(callback):
    '''Техника Орков'''

    orks_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Орки/Техника/main.jpg', 'rb'), caption=Orks_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_technics_inline)


def orks_squads(callback):
    '''Отряды Орков'''

    orks_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Орки/Отряды/main.jpg', 'rb'), caption=Orks_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_squads_inline)


def orks_characters(callback):
    '''Персонажи Орков'''

    orks_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Орки/Персонажи/main.jpg', 'rb'), caption=Orks_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_characters_inline)


def tau_main(callback):
    '''Меню Империи Тау'''

    tau_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='tau_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='tau_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='tau_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    tau_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Империя Тау/main.jpg', 'rb'), caption=Tau, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_inline)


def tau_technics(callback):
    '''Техника Империи Тау'''

    tau_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Империя Тау/Техника/main.jpg', 'rb'), caption=Tau_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_technics_inline)


def tau_squads(callback):
    '''Отряды Империи Тау'''

    tau_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Империя Тау/Отряды/main.jpg', 'rb'), caption=Tau_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_squads_inline)


def tau_characters(callback):
    '''Персонажи Империи Тау'''

    tau_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Империя Тау/Персонажи/main.jpg', 'rb'), caption=Tau_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_characters_inline)


def tiranidi_main(callback):
    '''Меню Тиранидов'''

    tiranidi_inline = types.InlineKeyboardMarkup(row_width=1)
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='tiranidi_squads')
    bugs = types.InlineKeyboardButton(text='Монстры', callback_data='tiranidi_monstrs')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    tiranidi_inline.add(squads, bugs, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Тираниды/main.jpg', 'rb'), caption=Tiranidi, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_inline)


def tiranidi_squads(callback):
    '''Отряды Тиранидов'''

    tiranidi_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tiranidi_main')
    tiranidi_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Тираниды/Отряды/main.jpg', 'rb'), caption=Tiranidi_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_squads_inline)


def tiranidi_monstrs(callback):
    '''Монстры Тиранидов'''

    tiranidi_ispolin_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tiranidi_main')
    tiranidi_ispolin_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии ксеносов/Тираниды/Монстры/main.jpg', 'rb'), caption=Tiranidi_Monstrs, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_ispolin_inline)
