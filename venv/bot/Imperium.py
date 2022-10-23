import telebot
from text import Imperium, Adeptus_Sosoritas, Sosoritas_Technics, Sosoritas_Squads, Sosoritas_Characters, Adeptus_Kustodes, \
Kustodes_Technics, Kustodes_Squads, Kustodes_Characters, Adeptus_Mechanikus, Mechanikus_Technics, Mechanikus_Squads, \
Mechanikus_Characters, Astra_Militarum, Militarum_Technics, Militarum_Squads, Militarum_Characters, Militarum_Upgrade, \
Knigts, Inquisition
from telebot import types
from config import TOKEN
from db import add_to_order


bot = telebot.TeleBot(TOKEN)


def imperium_main(callback):
    '''Меню Сил Империума'''

    imperium_inline = types.InlineKeyboardMarkup(row_width=1)
    sororitas = types.InlineKeyboardButton(text='Адептус сороритас', callback_data='sororitas_main')
    kustodes = types.InlineKeyboardButton(text='Адептус Кустодес', callback_data='kustodes_main')
    mechanikus = types.InlineKeyboardButton(text='Адептус механикус', callback_data='mechanikus_main')
    militarium = types.InlineKeyboardButton(text='Астра милитарум', callback_data='militarium_main')
    knigts = types.InlineKeyboardButton(text='Имперские рыцари', callback_data='knigts_main')
    inquisition = types.InlineKeyboardButton(text='Инквизиция', callback_data='inquisition_main')
    menu = types.InlineKeyboardButton(text='Назад ', callback_data='warhammer_menu')
    imperium_inline.add(sororitas, kustodes, mechanikus, militarium, knigts, inquisition, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/main.png', 'rb'), caption=Imperium, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=imperium_inline)


def sororitas_main(callback):
    '''Меню Адептус Сороритас'''

    sororitas_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='sororitas_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='sororitas_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='sororitas_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    sororitas_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус сороритас/main.jpeg', 'rb'), caption=Adeptus_Sosoritas, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_inline)


def sororitas_technics(callback):
    '''Техника Адептус Сороритас'''

    sororitas_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус сороритас/Техника/main.jpg', 'rb'), caption=Sosoritas_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_technics_inline)


def sororitas_squads(callback):
    '''Отряды Адептус Сороритас'''

    sororitas_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус сороритас/Отряды/main.jpg', 'rb'), caption=Sosoritas_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_squads_inline)


def sororitas_characters(callback):
    '''Персонажи Адептус Сороритас'''

    sororitas_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус сороритас/Персонажи/main.jpg', 'rb'), caption=Sosoritas_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_characters_inline)


def kustodes_main(callback):
    '''Меню Адептус Кустодес'''

    kustodes_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='kustodes_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='kustodes_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='kustodes_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    kustodes_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус кустодес/main.jpg', 'rb'), caption=Adeptus_Kustodes, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_inline)


def kustodes_technics(callback):
    '''Техника Адептус Кустодес'''

    kustodes_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус кустодес/Техника/main.jpg', 'rb'), caption=Kustodes_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_technics_inline)


def kustodes_squads(callback):
    '''Отряды Адептус Кустодес'''

    kustodes_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус кустодес/Отряды/main.jpg', 'rb'), caption=Kustodes_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_squads_inline)


def kustodes_characters(callback):
    '''Персонажи Адептус Кустодес'''

    kustodes_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус кустодес/Персонажи/main.jpg', 'rb'), caption=Kustodes_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_characters_inline)


def mechanikus_main(callback):
    '''Меню Адептус Механикус'''

    mechanikus_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='mechanikus_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='mechanikus_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='mechanikus_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    mechanikus_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус механикус/main.jpg', 'rb'), caption=Adeptus_Mechanikus, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup= mechanikus_inline)


def mechanikus_technics(callback):
    '''Техника Адептус Механикус'''

    mechanikus_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус механикус/Техника/main.jpg', 'rb'), caption=Mechanikus_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_technics_inline)


def mechanikus_squads(callback):
    '''Отряды Адептус Механикус'''

    mechanikus_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус механикус/Отряды/main.jpg', 'rb'), caption=Mechanikus_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_squads_inline)


def mechanikus_characters(callback):
    '''Персонажи Адептус Механикус'''

    mechanikus_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Адептус механикус/Персонажи/main.jpg', 'rb'), caption=Mechanikus_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_characters_inline)


def militarium_main(callback):
    '''Меню Астра Милитарум'''

    militarium_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='militarium_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='militarium_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='militarium_characters')
    upgrade = types.InlineKeyboardButton(text='Наборы апгрейда', callback_data='militarium_upgrade')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    militarium_inline.add(technics, squads, characters, upgrade, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Астра милитарум/main.jpg', 'rb'), caption=Astra_Militarum, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_inline)


def militarium_technics(callback):
    '''Техника Астра Милитарум'''

    militarium_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Астра милитарум/Техника/main.jpg', 'rb'), caption=Militarum_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_technics_inline)


def militarium_squads(callback):
    '''Отряды Астра Милитарум'''

    militarium_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Астра милитарум/Отряды/main.jpg', 'rb'), caption=Militarum_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_squads_inline)


def militarium_characters(callback):
    '''Персонажи Адептус Милитарум'''

    militarium_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Астра милитарум/Персонажи/main.jpg', 'rb'), caption=Militarum_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_characters_inline)


def militarium_upgrade(callback):
    '''Наборы апгрейда Адептус Милитарус'''

    militarium_upgrade_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_upgrade_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Астра милитарум/Наборы апгрейда/main.jpg', 'rb'), caption=Militarum_Upgrade, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_upgrade_inline)


def knigts_main(callback):
    '''Меню Имперских рыцарей'''

    knigts_inline = types.InlineKeyboardMarkup(row_width=4)
    knigt_15001 = types.InlineKeyboardButton(text='15001', callback_data='knigts_15001')
    knigt_15002 = types.InlineKeyboardButton(text='15002', callback_data='knigts_15002')
    knigt_15003 = types.InlineKeyboardButton(text='15003', callback_data='knigts_15003')
    knigt_15004 = types.InlineKeyboardButton(text='15004', callback_data='knigts_15004')
    knigt_15005 = types.InlineKeyboardButton(text='15005', callback_data='knigts_15005')
    knigt_15006 = types.InlineKeyboardButton(text='15006', callback_data='knigts_15006')
    knigt_15007 = types.InlineKeyboardButton(text='15007', callback_data='knigts_15007')
    knigt_15008 = types.InlineKeyboardButton(text='15008', callback_data='knigts_15008')
    knigt_15009 = types.InlineKeyboardButton(text='15009', callback_data='knigts_15009')
    knigt_15010 = types.InlineKeyboardButton(text='15010', callback_data='knigts_15010')
    knigt_15011 = types.InlineKeyboardButton(text='15011', callback_data='knigts_15011')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    knigts_inline.add(knigt_15001, knigt_15002, knigt_15003, knigt_15004, knigt_15005, knigt_15006, knigt_15007,
                      knigt_15008, knigt_15009, knigt_15010, knigt_15011, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/main.jpg', 'rb'), caption=Knigts, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_inline)


def knigts_15001(callback):
    '''Имперский рыцарь 15001'''
    
    knigts_15001_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15001')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15001_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15001.jpg', 'rb'), caption='Индекс: 15001\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15001_inline)

def add_15001(callback):
    '''Добавление в корзину имперского рыцаря 15001'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15001, ')


def knigts_15002(callback):
    '''Имперский рыцарь 15002'''
    
    knigts_15002_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15002')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15002_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15002.jpg', 'rb'), caption='Индекс: 15002\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15002_inline)

def add_15002(callback):
    '''Добавление в корзину имперского рыцаря 15002'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15002, ')


def knigts_15003(callback):
    '''Имперский рыцарь 15003'''

    knigts_15003_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15003')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15003_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15003.jpg', 'rb'), caption='Индекс: 15003\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15003_inline)

def add_15003(callback):
    '''Добавление в корзину имперского рыцаря 15003'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15003, ')


def knigts_15004(callback):
    '''Имперский рыцарь 15004'''

    knigts_15004_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15004')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15004_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15004.jpg', 'rb'), caption='Индекс: 15004\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15004_inline)

def add_15004(callback):
    '''Добавление в корзину имперского рыцаря 15004'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15004, ')


def knigts_15005(callback):
    '''Имперский рыцарь 15005'''

    knigts_15005_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15005')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15005_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15005.jpg', 'rb'), caption='Индекс: 15005\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15005_inline)

def add_15005(callback):
    '''Добавление в корзину имперского рыцаря 15005'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15005, ')


def knigts_15006(callback):
    '''Имперский рыцарь 15006'''

    knigts_15006_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15006')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15006_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15006.jpg', 'rb'), caption='Индекс: 15006\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15006_inline)

def add_15006(callback):
    '''Добавление в корзину имперского рыцаря 15006'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15006, ')


def knigts_15007(callback):
    '''Имперский рыцарь 15007'''

    knigts_15007_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15007')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15007_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15007.jpg', 'rb'), caption='Индекс: 15007\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15007_inline)

def add_15007(callback):
    '''Добавление в корзину имперского рыцаря 15007'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15007, ')


def knigts_15008(callback):
    '''Имперский рыцарь 15008'''

    knigts_15008_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15008')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15008_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15008.jpg', 'rb'), caption='Индекс: 15008\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15008_inline)

def add_15008(callback):
    '''Добавление в корзину имперского рыцаря 15008'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15008, ')


def knigts_15009(callback):
    '''Имперский рыцарь 15009'''

    knigts_15009_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15009')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15009_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15009.jpg', 'rb'), caption='Индекс: 15009\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15009_inline)

def add_15009(callback):
    '''Добавление в корзину имперского рыцаря 15009'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15009, ')


def knigts_15010(callback):
    '''Имперский рыцарь 15010'''

    knigts_15010_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15010')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15010_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15010.jpg', 'rb'), caption='Индекс: 15010\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15010_inline)

def add_15010(callback):
    '''Добавление в корзину имперского рыцаря 15010'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15010, ')


def knigts_15011(callback):
    '''Имперский рыцарь 15011'''

    knigts_15011_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_15011')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15011_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Имперские рыцари/15011.jpg', 'rb'), caption='Индекс: 15011\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15011_inline)

def add_15011(callback):
    '''Добавление в корзину имперского рыцаря 15011'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '15011, ')


def inquisition_main(callback):
    '''Меню Инквизиции'''

    inquisition_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    inquisition_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Силы Империума/Инквизиция/main.jpeg', 'rb'), caption=Inquisition, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=inquisition_inline)
