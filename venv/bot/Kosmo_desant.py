import telebot
from telebot import types
from config import TOKEN, START, DELIVERY, ORDER

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

def main_menu(callback):
    main_inline = types.InlineKeyboardMarkup(row_width=1)
    desant = types.InlineKeyboardButton(text='Космодесант', callback_data='kosmo')
    imp = types.InlineKeyboardButton(text='Силы Империума', callback_data='imperium')
    Order = types.InlineKeyboardButton(text='Сделать заказ', callback_data='order')
    Delivery = types.InlineKeyboardButton(text='Доставка', callback_data='delivery')
    main_inline.add(desant, imp, Order, Delivery)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=START, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=main_inline)

def order(callback):
    order_inline = types.InlineKeyboardMarkup(row_width=1)
    menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
    order_inline.add(menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=ORDER, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=order_inline)


def delivery(callback):
    delivery_inline = types.InlineKeyboardMarkup(row_width=1)
    menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
    delivery_inline.add(menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=DELIVERY, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=delivery_inline)

def kosmo_main(callback):
    kosmo_inline = types.InlineKeyboardMarkup(row_width=1)
    Kosmo_units = types.InlineKeyboardButton(text='Общие Юниты', callback_data='kosmo_units')
    Orden_kosmo = types.InlineKeyboardButton(text='Отряды орденов космодесанта', callback_data='orden_kosmo')
    menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
    kosmo_inline.add(Kosmo_units, Orden_kosmo, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/kosmodesant.png', 'rb'), caption=KOSMO_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_inline)


def kosmo_units(callback):
    kosmo_units_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='back_from_kosmo_units')
    kosmo_units_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/kosmounits.png', 'rb'), caption=KOSMO_UNITS_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_units_inline)


def back_from_kosmo_units(callback):
    kosmo_main(callback)


def orden_kosmo(callback):
    kosmo_orden_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='back_from_orden_kosmo')
    kosmo_orden_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/kosmoorden.png', 'rb'), caption=KOSMO_ORDEN_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=kosmo_orden_inline)

def back_from_orden_kosmo(callback):
    kosmo_main(callback)
































