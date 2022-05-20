import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def ksenos_main(callback):
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
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Армии ксеносов', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=ksenos_inline)


def aeldari_main(callback):
    aeldari_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='aeldari_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='aeldari_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='aeldari_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    aeldari_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='елдари', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_inline)


def aeldari_technics(callback):
    aeldari_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_technics_inline)


def aeldari_squads(callback):
    aeldari_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_squads_inline)


def aeldari_characters(callback):
    aeldari_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='aeldari_main')
    aeldari_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=aeldari_characters_inline)


def drukhari_main(callback):
    drukhari_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='drukhari_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='drukhari_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='drukhari_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    drukhari_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='друкхари', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_inline)


def drukhari_technics(callback):
    drukhari_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_technics_inline)


def drukhari_squads(callback):
    drukhari_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_squads_inline)


def drukhari_characters(callback):
    drukhari_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='drukhari_main')
    drukhari_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=drukhari_characters_inline)


def genokradi_main(callback):
    genokradi_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='genokradi_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='genokradi_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='genokradi_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    genokradi_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='генокрад букин', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_inline)


def genokradi_technics(callback):
    genokradi_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_technics_inline)


def genokradi_squads(callback):
    genokradi_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_squads_inline)


def genokradi_characters(callback):
    genokradi_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='genokradi_main')
    genokradi_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=genokradi_characters_inline)


def necroni_main(callback):
    necroni_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='necroni_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='necroni_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='necroni_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    necroni_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Некроны', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_inline)


def necroni_technics(callback):
    necroni_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_technics_inline)


def necroni_squads(callback):
    necroni_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_squads_inline)


def necroni_characters(callback):
    necroni_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='necroni_main')
    necroni_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=necroni_characters_inline)


def orks_main(callback):
    orks_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='orks_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='orks_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='orks_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    orks_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Орки', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_inline)


def orks_technics(callback):
    orks_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_technics_inline)


def orks_squads(callback):
    orks_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_squads_inline)


def orks_characters(callback):
    orks_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orks_main')
    orks_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orks_characters_inline)


def tau_main(callback):
    tau_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='tau_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='tau_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='tau_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    tau_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Империя тау', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_inline)


def tau_technics(callback):
    tau_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_technics_inline)


def tau_squads(callback):
    tau_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_squads_inline)


def tau_characters(callback):
    tau_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tau_main')
    tau_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tau_characters_inline)


def tiranidi_main(callback):
    tiranidi_inline = types.InlineKeyboardMarkup(row_width=1)
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='tiranidi_squads')
    bugs = types.InlineKeyboardButton(text='Большие жуки', callback_data='tiranidi_bugs')
    back = types.InlineKeyboardButton(text='Назад', callback_data='ksenos_main')
    tiranidi_inline.add(squads, bugs, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Тираниды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_inline)


def tiranidi_squads(callback):
    tiranidi_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tiranidi_main')
    tiranidi_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_squads_inline)


def tiranidi_bugs(callback):
    tiranidi_bugs_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='tiranidi_main')
    tiranidi_bugs_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Большие жуки', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=tiranidi_bugs_inline)
