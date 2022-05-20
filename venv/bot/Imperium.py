import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

IMPERIUM_TEXT = '''Империум — самое большое государство в галактике, насчитывающее более миллиона звёздных систем, находящихся в Галактике Млечного Пути и раздёленных между собой многими световыми годами. 
Размер Империума как межзвёздного государства исчисляется не протяжённостью территорий, а именно звёздными системами, которые он контролирует. 
Столицей Империума является родина человечества Священная Терра'''

ADEPTUS_TEXT = '''Адептус Механикус — технократическая организация, также известная как Духовенство Марса. 
Она удерживает монополию на технологические знания в Империуме. Их миры-кузни производят самое мощное и продвинутое вооружение Империума. 
Адепты этой организации, техножрецы, жизненно необходимы в поддержке большинства наиболее продвинутых технологий Империума, далеко не последней из которых является поддерживающий жизнь Императора Золотой Трон.'''

ASTRA_TEXT = '''Гвардия — основа Империума, несомненно, что без неё человечество бы погибло. 
И хотя гвардейцы не идут ни в какое сравнение с космодесантниками, сражаясь без использования генетических улучшений и лучшего персонального вооружения, 
у Гвардии достаточно храбрости и людских ресурсов для того, чтобы встретить и уничтожить врагов Императора по всей галактике'''


def imperium_main(callback):
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
        media=types.InputMedia(media=open('pictures/imperium.png', 'rb'), caption=IMPERIUM_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=imperium_inline)


def sororitas_main(callback):
    sororitas_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='sororitas_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='sororitas_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='sororitas_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    sororitas_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Сосоритас', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_inline)


def sororitas_technics(callback):
    sororitas_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_technics_inline)


def sororitas_squads(callback):
    sororitas_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_squads_inline)



def sororitas_characters(callback):
    sororitas_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='sororitas_main')
    sororitas_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=sororitas_characters_inline)


def kustodes_main(callback):
    kustodes_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='kustodes_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='kustodes_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='kustodes_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    kustodes_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Кустодес', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_inline)


def kustodes_technics(callback):
    kustodes_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_technics_inline)


def kustodes_squads(callback):
    kustodes_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_squads_inline)



def kustodes_characters(callback):
    kustodes_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kustodes_main')
    kustodes_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kustodes_characters_inline)

def mechanikus_main(callback):
    mechanikus_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='mechanikus_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='mechanikus_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='mechanikus_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    mechanikus_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='механикус', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup= mechanikus_inline)


def mechanikus_technics(callback):
    mechanikus_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_technics_inline)


def mechanikus_squads(callback):
    mechanikus_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_squads_inline)



def mechanikus_characters(callback):
    mechanikus_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    mechanikus_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=mechanikus_characters_inline)


def militarium_main(callback):
    militarium_inline = types.InlineKeyboardMarkup(row_width=1)
    technics = types.InlineKeyboardButton(text='Техника', callback_data='militarium_technics')
    squads = types.InlineKeyboardButton(text='Отряды', callback_data='militarium_squads')
    characters = types.InlineKeyboardButton(text='Персонажи', callback_data='militarium_characters')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    militarium_inline.add(technics, squads, characters, back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='милитарум', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_inline)


def militarium_technics(callback):
    militarium_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='mechanikus_main')
    militarium_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_technics_inline)


def militarium_squads(callback):
    militarium_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_squads_inline)



def militarium_characters(callback):
    militarium_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_characters_inline)

def knigts_main(callback):
    knigts_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    knigts_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='рыцари', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_inline)


def inquisition_main(callback):
    inquisition_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    inquisition_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='инквизиторы', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=inquisition_inline)



