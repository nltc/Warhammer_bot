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
    upgrade = types.InlineKeyboardButton(text='Наборы апгрейда', callback_data='militarium_upgrade')
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    militarium_inline.add(technics, squads, characters, upgrade, back)
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


def militarium_upgrade(callback):
    militarium_upgrade_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='militarium_main')
    militarium_upgrade_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Наборы апгрейда', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=militarium_upgrade_inline)


def knigts_main(callback):
    knigts_inline = types.InlineKeyboardMarkup(row_width=1)
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
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='рыцари', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_inline)

def knigts_15001(callback):
    knigts_15001_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15001_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15001.jpg', 'rb'), caption='Индекс: 15001\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15001_inline)


def knigts_15002(callback):
    knigts_15002_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15002_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15002.jpg', 'rb'), caption='Индекс: 15002\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15002_inline)


def knigts_15003(callback):
    knigts_15003_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15003_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15003.jpg', 'rb'), caption='Индекс: 15003\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15003_inline)


def knigts_15004(callback):
    knigts_15004_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15004_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15004.jpg', 'rb'), caption='Индекс: 15004\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15004_inline)


def knigts_15005(callback):
    knigts_15005_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15005_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15005.jpg', 'rb'), caption='Индекс: 15005\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15005_inline)


def knigts_15006(callback):
    knigts_15006_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15006_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15006.jpg', 'rb'), caption='Индекс: 15006\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15006_inline)


def knigts_15007(callback):
    knigts_15007_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15007_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15007.jpg', 'rb'), caption='Индекс: 15007\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15007_inline)


def knigts_15008(callback):
    knigts_15008_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15008_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15008.jpg', 'rb'), caption='Индекс: 15008\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15008_inline)


def knigts_15009(callback):
    knigts_15009_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15009_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15009.jpg', 'rb'), caption='Индекс: 15009\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15009_inline)


def knigts_15010(callback):
    knigts_15010_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15010_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15010.jpg', 'rb'), caption='Индекс: 15010\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15010_inline)


def knigts_15011(callback):
    knigts_15011_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='knigts_main')
    knigts_15011_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('Имперские рыцари/15011.jpg', 'rb'), caption='Индекс: 15011\nЦена: 4999 руб.', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=knigts_15011_inline)







def inquisition_main(callback):
    inquisition_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='imperium_main')
    inquisition_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='инквизиторы', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=inquisition_inline)



