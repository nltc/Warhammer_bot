import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def chaos_main(callback):
    chaos_inline = types.InlineKeyboardMarkup(row_width=1)
    demons = types.InlineKeyboardButton(text='Демоны хаоса', callback_data='demons_main')
    knights_chaos = types.InlineKeyboardButton(text='Рыцари хаоса', callback_data='knights_chaos_main')
    kosmo_chaos = types.InlineKeyboardButton(text='Космодесант хаоса', callback_data='kosmo_chaos_main')
    guard_death = types.InlineKeyboardButton(text='Гвардия смерти', callback_data='guard_death_main')
    thousand_sons = types.InlineKeyboardButton(text='Тысяча сынов', callback_data='thousand_sons_main')
    menu = types.InlineKeyboardButton(text='Назад', callback_data='warhammer_menu')
    chaos_inline.add(demons, knights_chaos, kosmo_chaos, guard_death, thousand_sons, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Армия хаоса', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=chaos_inline)


def demons_main(callback):
    demons_inline = types.InlineKeyboardMarkup(row_width=1)
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='demons_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='demons_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    demons_inline.add(squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='демонюги', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_inline)

def demons_squads(callback):
    demons_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='demons_main')
    demons_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_squads_inline)


def demons_characters(callback):
    demons_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='demons_main')
    demons_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_characters_inline)


def knights_chaos_main(callback):
    knights_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    knights_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='рыцарюги', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_inline)


def kosmo_chaos_main(callback):
    kosmo_chaos_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='kosmo_chaos_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='kosmo_chaos_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='kosmo_chaos_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    kosmo_chaos_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='космодесант хаоса', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_inline)


def kosmo_chaos_technics(callback):
    kosmo_chaos_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_technics_inline)


def kosmo_chaos_squads(callback):
    kosmo_chaos_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_squads_inline)


def kosmo_chaos_characters(callback):
    kosmo_chaos_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_characters_inline)

def guard_death_main(callback):
    guard_death_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='guard_death_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='guard_death_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='guard_death_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    guard_death_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='гвардия смерти', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_inline)


def guard_death_technics(callback):
    guard_death_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_technics_inline)


def guard_death_squads(callback):
    guard_death_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_squads_inline)


def guard_death_characters(callback):
    guard_death_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_characters_inline)

def thousand_sons_main(callback):
    thousand_sons_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='thousand_sons_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='thousand_sons_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='thousand_sons_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    thousand_sons_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='сынки', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_inline)


def thousand_sons_technics(callback):
    thousand_sons_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_technics_inline)


def thousand_sons_squads(callback):
    thousand_sons_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_squads_inline)


def thousand_sons_characters(callback):
    thousand_sons_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_characters_inline)

