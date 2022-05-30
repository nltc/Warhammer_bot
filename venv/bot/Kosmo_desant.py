import telebot
from telebot import types
from config import TOKEN
from db import add_to_order

bot = telebot.TeleBot(TOKEN)


KOSMO_TEXT = '''Аде́птус Аста́ртес  — одни из самых элитных и устрашающих вооружённых сил Империума. 
Основная организационная единица Астартес — орден, самостоятельная армия. 
Существует более тысячи орденов, но всё равно этого слишком мало для того, чтобы считать космических десантников основной военной силой Империума. 
Вместо этого они выступают в роли высокомобильных ударных сил. 
Им поручают выполнение самых опасных заданий, таких как молниеносные рейды в тылу противника, операции по проникновению и битвы в замкнутых пространствах. 
Космодесантники проходят жесточайший отбор, тренировки, духовную и психическую подготовку и в десятки раз превосходят других воинов Империума'''

KOSMO_UNITS_TEXT = '''Традиционный кодексный орден имеет в своём составе различные виды отделений: тактические, штурмовые и отделения опустошителей. 
Каждое отделение подготавливается и экипируется таким образом, чтобы выполнять специфическую роль на поле боя, 
каждый из трёх видов отделений дополняет друг друга в сражении и вместе они составляют единый организм, невероятно мощный и эффективный. 
Также, в дополнение к основным видам отделений, из воинов-ветеранов могут быть сформированы отделения ветеранов или терминаторов, а из новобранцев-космодесантников создают отделения скаутов.'''

KOSMO_ORDEN_TEXT = '''Орден Адептус Астартес — самостоятельная организационная единица космического десанта, 
обычно состоящая примерно из тысячи космодесантников, включающая в себя также административный и вспомогательный персонал. 
На данный момент Адептус Астартес разделены примерно на тысячу орденов. Каждый орден полностью автономен, имеет свое командование, традиции, специализацию и мировоззрение'''


def kosmo_main(callback):

    '''Меню Космодесанта'''

    kosmo_inline = types.InlineKeyboardMarkup(row_width=1)
    Kosmo_units = types.InlineKeyboardButton(text='Общие Юниты', callback_data='kosmo_units')
    Orden_kosmo = types.InlineKeyboardButton(text='Отдельные ордена', callback_data='orden_kosmo')
    menu = types.InlineKeyboardButton(text='Назад', callback_data='warhammer_menu')
    kosmo_inline.add(Kosmo_units, Orden_kosmo, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/kosmodesant.png', 'rb'), caption=KOSMO_TEXT, type="photo"),
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
        media=types.InputMedia(media=open('pictures/kosmounits.png', 'rb'), caption=KOSMO_UNITS_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_units_inline)


def kosmo_units_technics(callback):

    '''Техника общих юнитов'''

    kosmo_units_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_units_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_units_technics_inline)


def kosmo_squads(callback):

    '''Отряды общих юнитов'''

    kosmo_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_squads_inline)



def kosmo_characters(callback):

    '''Персонажи общих юнитов'''

    kosmo_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='kosmo_units')
    kosmo_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
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
        media=types.InputMedia(media=open('pictures/kosmoorden.png', 'rb'), caption=KOSMO_ORDEN_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_orden_inline)


def orden_technics(callback):

    '''Техника отдельных орденов'''

    kosmo_orden_technics_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    kosmo_orden_technics_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Техника', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_orden_technics_inline)


def orden_squads(callback):

    '''Отряды отдельных орденов'''

    orden_squads_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_squads_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Отряды', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_squads_inline)



def orden_characters(callback):

    '''Персонажи отдельных орденов'''

    orden_characters_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_characters_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Персонажи', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_characters_inline)


def orden_upgrade(callback):

    '''Наборы апргейда отдельных орденов'''

    orden_upgrade_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='orden_kosmo')
    orden_upgrade_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption='Наборы апргейда', type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=orden_upgrade_inline)



































