import telebot
from text import Adeptus, Units, Technics, Squads, Characters, Orden, Orden_Upgrade, Orden_Technics, Orden_Squads, Orden_Characters, Orden_Upgrade
from telebot import types
from config import TOKEN
from db import add_to_order


bot = telebot.TeleBot(TOKEN)


def kosmo_main(callback):

    '''Меню Космодесанта'''

    kosmo_inline = types.InlineKeyboardMarkup(row_width=1)
    Kosmo_units = types.InlineKeyboardButton(text='Общие Юниты', callback_data='kosmo_units')
    Orden_kosmo = types.InlineKeyboardButton(text='Отдельные ордена', callback_data='orden_kosmo')
    menu = types.InlineKeyboardButton(text='Назад', callback_data='warhammer_menu')
    kosmo_inline.add(Kosmo_units, Orden_kosmo, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/main.jpg', 'rb'), caption=Adeptus, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_inline)


def kosmo_units(callback):

    '''Меню общих юнитов'''

    kosmo_units_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='kosmo_units_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='kosmo_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='kosmo_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_main')
    kosmo_units_inline.add(technics,squads,characters,back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Общие юниты/main.jpg', 'rb'), caption=Units, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_units_inline)


def kosmo_units_technics(callback):

    '''Техника общих юнитов'''

    kosmo_units_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_units_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Общие юниты/Техника/main.jpg', 'rb'), caption=Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_units_technics_inline)


def kosmo_squads(callback):

    '''Отряды общих юнитов'''

    kosmo_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Общие юниты/Отряды/main.JPG', 'rb'), caption=Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_squads_inline)



def kosmo_characters(callback):

    '''Персонажи общих юнитов'''

    kosmo_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Общие юниты/Персонажи/main.jpg', 'rb'), caption=Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_characters_inline)



def orden_kosmo(callback):

    '''Меню отдельных орденов'''

    kosmo_orden_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='orden_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='orden_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='orden_characters')
    upgrade = types.InlineKeyboardButton(text='Наборы апгрейда', callback_data='orden_upgrade')
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_main')
    kosmo_orden_inline.add(technics, squads, characters, upgrade,back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Отдельные ордена/main.jpeg', 'rb'), caption=Orden, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_orden_inline)


def orden_technics(callback):

    '''Техника отдельных орденов'''

    kosmo_orden_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    kosmo_orden_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Отдельные ордена/Техника/main.JPG', 'rb'), caption=Orden_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_orden_technics_inline)


def orden_squads(callback):

    '''Отряды отдельных орденов'''

    orden_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Отдельные ордена/Отряды/main.JPG', 'rb'), caption=Orden_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_squads_inline)



def orden_characters(callback):

    '''Персонажи отдельных орденов'''

    orden_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Отдельные ордена/Персонажи/main.JPG', 'rb'), caption=Orden_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_characters_inline)


def orden_upgrade(callback):

    '''Наборы апргейда отдельных орденов'''

    orden_upgrade_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_upgrade_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Космодесант/Отдельные ордена/Наборы апгрейда/main.JPG', 'rb'), caption=Orden_Upgrade, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_upgrade_inline)



































