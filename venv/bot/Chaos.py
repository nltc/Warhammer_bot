import telebot
from text import Chaos, Demons, Demons_Squads, Demons_Characters, Knigts_Chaos, Kosmo_Chaos, Kosmo_Chaos_Technics, \
Kosmo_Chaos_Squads, Kosmo_Chaos_Characters, Guard_Death, Guard_Death_Technics, Guard_Death_Squads, Guard_Death_Characters, \
Thousand_Sons, Thousand_Sons_Technics, Thousand_Sons_Squads, Thousand_Sons_Characters, Chaos_Upgrade
from telebot import types
from config import TOKEN
from db import add_to_order


bot = telebot.TeleBot(TOKEN)


def chaos_main(callback):
    '''Меню армии хаоса'''

    chaos_inline = types.InlineKeyboardMarkup(row_width=1)
    demons = types.InlineKeyboardButton(text='Демоны хаоса', callback_data='demons_main')
    knights_chaos = types.InlineKeyboardButton(text='Рыцари хаоса', callback_data='knights_chaos_main')
    kosmo_chaos = types.InlineKeyboardButton(text='Космодесант хаоса', callback_data='kosmo_chaos_main')
    guard_death = types.InlineKeyboardButton(text='Гвардия смерти', callback_data='guard_death_main')
    thousand_sons = types.InlineKeyboardButton(text='Тысяча сынов', callback_data='thousand_sons_main')
    upgrade = types.InlineKeyboardButton(text='Наборы апгрейда', callback_data='upgrade_main')
    menu = types.InlineKeyboardButton(text='Назад', callback_data='warhammer_menu')
    chaos_inline.add(demons, knights_chaos, kosmo_chaos, guard_death, thousand_sons,upgrade, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/main.gif', 'rb'), caption=Chaos, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=chaos_inline)


def demons_main(callback):
    '''Меню демонов'''

    demons_inline = types.InlineKeyboardMarkup(row_width=1)
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='demons_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='demons_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    demons_inline.add(squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Демоны хаоса/main.jpg', 'rb'), caption=Demons, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_inline)


def demons_squads(callback):
    '''Отряды демонов'''

    demons_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='demons_main')
    demons_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Демоны хаоса/Отряды/main.jpg', 'rb'), caption=Demons_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_squads_inline)


def demons_characters(callback):
    '''Персонажи демонов'''

    demons_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='demons_main')
    demons_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Демоны хаоса/Персонажи/main.jpg', 'rb'), caption=Demons_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=demons_characters_inline)


def knights_chaos_main(callback):
    '''Меню рыцарей хаоса'''

    knights_inline = types.InlineKeyboardMarkup(row_width=4)
    knights_chaos_22001 = types.InlineKeyboardButton(text='22001', callback_data='knights_chaos_22001')
    knights_chaos_22002 = types.InlineKeyboardButton(text='22002', callback_data='knights_chaos_22002')
    knights_chaos_22003 = types.InlineKeyboardButton(text='22003', callback_data='knights_chaos_22003')
    knights_chaos_22004 = types.InlineKeyboardButton(text='22004', callback_data='knights_chaos_22004')
    knights_chaos_22005 = types.InlineKeyboardButton(text='22005', callback_data='knights_chaos_22005')
    knights_chaos_22006 = types.InlineKeyboardButton(text='22006', callback_data='knights_chaos_22006')
    knights_chaos_22007 = types.InlineKeyboardButton(text='22007', callback_data='knights_chaos_22007')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    knights_inline.add(knights_chaos_22001, knights_chaos_22002, knights_chaos_22003, knights_chaos_22004, knights_chaos_22005,
                        knights_chaos_22006, knights_chaos_22007,back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/main.jpg', 'rb'), caption=Knigts_Chaos, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_inline)


def knights_chaos_22001(callback):
    '''Рыцарь хаоса 22001'''

    knights_chaos_22001_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22001')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22001_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22001.jpg', 'rb'), caption='Индекс: 22001\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22001_inline)

def add_22001(callback):
    '''Добавление в корзину рыцаря хаоса 22001'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22001, ')



def knights_chaos_22002(callback):
    '''Рыцарь хаоса 22002'''

    knights_chaos_22002_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22002')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22002_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22002.jpg', 'rb'), caption='Индекс: 22002\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22002_inline)

def add_22002(callback):
    '''Добавление в корзину рыцаря хаоса 22002'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22002, ')


def knights_chaos_22003(callback):
    '''Рыцарь хаоса 22003'''

    knights_chaos_22003_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22003')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22003_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22003.jpg', 'rb'), caption='Индекс: 22003\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22003_inline)

def add_22003(callback):
    '''Добавление в корзину рыцаря хаоса 22003'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22003, ')


def knights_chaos_22004(callback):
    '''Рыцарь хаоса 22004'''

    knights_chaos_22004_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22004')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22004_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22004.jpg', 'rb'), caption='Индекс: 22004\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22004_inline)

def add_22004(callback):
    '''Добавление в корзину рыцаря хаоса 22004'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22004, ')


def knights_chaos_22005(callback):
    '''Рыцарь хаоса 22005'''

    knights_chaos_22005_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22005')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22005_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22005.jpg', 'rb'), caption='Индекс: 22005\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22005_inline)

def add_22005(callback):
    '''Добавление в корзину рыцаря хаоса 22005'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22005, ')


def knights_chaos_22006(callback):
    '''Рыцарь хаоса 22006'''

    knights_chaos_22006_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22006')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22006_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22006.jpg', 'rb'), caption='Индекс: 22006\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22006_inline)

def add_22006(callback):
    '''Добавление в корзину рыцаря хаоса 22006'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22006, ')


def knights_chaos_22007(callback):
    '''Рыцарь хаоса 22007'''

    knights_chaos_22007_inline = types.InlineKeyboardMarkup(row_width=1)
    add = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add_22007')
    back = types.InlineKeyboardButton(text='Назад', callback_data='knights_chaos_main')
    knights_chaos_22007_inline.add(add, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Рыцари хаоса/22007.jpg', 'rb'), caption='Индекс: 22007\nЦена: 4999 руб.',
                               type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knights_chaos_22007_inline)

def add_22007(callback):
    '''Добавление в корзину рыцаря хаоса 22007'''

    bot.answer_callback_query(callback_query_id=callback.id, text="Добавлено в корзину", show_alert=False)
    add_to_order(callback, '22007, ')


def kosmo_chaos_main(callback):
    '''Меню космодесанта хаоса'''

    kosmo_chaos_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='kosmo_chaos_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='kosmo_chaos_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='kosmo_chaos_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    kosmo_chaos_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Космодесант хаоса/main.jpg', 'rb'), caption=Kosmo_Chaos, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_inline)


def kosmo_chaos_technics(callback):
    '''Техника космодесанта хаоса'''

    kosmo_chaos_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Космодесант хаоса/Техника/main.jpg', 'rb'), caption=Kosmo_Chaos_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_technics_inline)


def kosmo_chaos_squads(callback):
    '''Отряды космодесанта хаоса'''

    kosmo_chaos_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Космодесант хаоса/Отряды/main.jpg', 'rb'), caption=Kosmo_Chaos_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_squads_inline)


def kosmo_chaos_characters(callback):
    '''Персонажи космодесанта хаоса'''

    kosmo_chaos_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_chaos_main')
    kosmo_chaos_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Космодесант хаоса/Персонажи/main.png', 'rb'), caption=Kosmo_Chaos_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_chaos_characters_inline)


def guard_death_main(callback):
    '''Меню гвардии смерти'''

    guard_death_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='guard_death_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='guard_death_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='guard_death_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    guard_death_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Гвардия смерти/main.jpg', 'rb'), caption=Guard_Death, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_inline)


def guard_death_technics(callback):
    '''Техника гвардии смерти'''

    guard_death_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Гвардия смерти/Техника/main.jpg', 'rb'), caption=Guard_Death_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_technics_inline)


def guard_death_squads(callback):
    '''Отряды гвардии смерти'''

    guard_death_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Гвардия смерти/Отряды/main.png', 'rb'), caption=Guard_Death_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_squads_inline)


def guard_death_characters(callback):
    '''Персонажи гвардии смерти'''

    guard_death_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='guard_death_main')
    guard_death_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Гвардия смерти/Персонажи/main.png', 'rb'), caption=Guard_Death_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=guard_death_characters_inline)


def thousand_sons_main(callback):
    '''Меню тысячи сынов'''

    thousand_sons_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='thousand_sons_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='thousand_sons_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='thousand_sons_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    thousand_sons_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Тысяча сынов/main.jpg', 'rb'), caption=Thousand_Sons, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_inline)


def thousand_sons_technics(callback):
    '''Техника тысячи сынов'''

    thousand_sons_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Тысяча сынов/Техника/main.jpg', 'rb'), caption=Thousand_Sons_Technics, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_technics_inline)


def thousand_sons_squads(callback):
    '''Отряды тысячи сынов'''

    thousand_sons_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Тысяча сынов/Отряды/main.jpg', 'rb'), caption=Thousand_Sons_Squads, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_squads_inline)


def thousand_sons_characters(callback):
    '''Персонажи тысячи сынов'''

    thousand_sons_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='thousand_sons_main')
    thousand_sons_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Тысяча сынов/Персонажи/main.jpg', 'rb'), caption=Thousand_Sons_Characters, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=thousand_sons_characters_inline)


def upgrade_main(callback):
    '''Меню наборов апргейда'''

    upgrade_main_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='chaos_main')
    upgrade_main_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/Армии Хаоса/Наборы апгрейда/main.jpg', 'rb'), caption=Chaos_Upgrade, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=upgrade_main_inline)

