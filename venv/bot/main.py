import telebot
from telebot import types
from config import TOKEN, START, DELIVERY, ORDER
from Kosmo_desant import KOSMO_TEXT
from Imperium import IMPERIUM_TEXT


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    desant = types.InlineKeyboardButton(text ='Космодесант', callback_data='kosmo')
    imp = types.InlineKeyboardButton(text='Силы Империума', callback_data='imperium')
    Order = types.InlineKeyboardButton(text='Сделать заказ', callback_data='order')
    Delivery = types.InlineKeyboardButton(text='Доставка', callback_data='delivery')
    markup_inline.add(desant,imp,Order,Delivery)
    bot.send_photo(message.chat.id, photo=open('pictures/start.png', 'rb'), caption=START, reply_markup= markup_inline)


@bot.callback_query_handler(func = lambda callback: callback.data)
def main(callback):
    if callback.data == 'kosmo':
        markup_inline_2 = types.InlineKeyboardMarkup(row_width=1)
        Kosmo_units = types.InlineKeyboardButton(text='Общие Юниты', callback_data='kosmo_units')
        Orden_kosmo = types.InlineKeyboardButton(text='Отряды орденов космодесанта', callback_data='orden_kosmo')
        menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
        markup_inline_2.add(Kosmo_units, Orden_kosmo, menu)

        bot.edit_message_media(media=types.InputMedia(media=open('pictures/kosmodesant.png', 'rb'), caption=KOSMO_TEXT, type="photo"), chat_id=callback.message.chat.id, message_id=callback.message.id,
                              reply_markup=markup_inline_2)
    elif callback.data == 'imperium':
        markup_inline_3 = types.InlineKeyboardMarkup(row_width=1)
        Astra = types.InlineKeyboardButton(text='Астра милитарум (имперская гвардия)', callback_data='astra')
        Adeptus = types.InlineKeyboardButton(text='Адептус механикус', callback_data='adeptus')
        menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
        markup_inline_3.add(Astra, Adeptus, menu)
        bot.edit_message_media(
            media=types.InputMedia(media=open('pictures/imperium.png', 'rb'), caption=IMPERIUM_TEXT, type="photo"),
            chat_id=callback.message.chat.id, message_id=callback.message.id,
            reply_markup=markup_inline_3)

    elif callback.data == 'menu':
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        desant = types.InlineKeyboardButton(text='Космодесант', callback_data='kosmo')
        imp = types.InlineKeyboardButton(text='Силы Империума', callback_data='imperium')
        Order = types.InlineKeyboardButton(text='Сделать заказ', callback_data='order')
        Delivery = types.InlineKeyboardButton(text='Доставка', callback_data='delivery')
        markup_inline.add(desant, imp, Order, Delivery)
        bot.edit_message_media(
            media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=START, type="photo"),
            chat_id=callback.message.chat.id, message_id=callback.message.id,
            reply_markup=markup_inline)

    elif callback.data == 'order':
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
        markup_inline.add(menu)
        bot.edit_message_media(
            media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=ORDER, type="photo"),
            chat_id=callback.message.chat.id, message_id=callback.message.id,
            reply_markup=markup_inline)

    elif callback.data == 'delivery':
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
        markup_inline.add(menu)
        bot.edit_message_media(
            media=types.InputMedia(media=open('pictures/start.png', 'rb'), caption=DELIVERY, type="photo"),
            chat_id=callback.message.chat.id, message_id=callback.message.id,
            reply_markup=markup_inline)



bot.infinity_polling()
# bot.polling(none_stop=True, interval=0)