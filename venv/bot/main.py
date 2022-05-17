import telebot
from telebot import types
from config import TOKEN, START
from Kosmo_desant import kosmo_main, back_from_kosmo_units, kosmo_units, orden_kosmo, main_menu, order, delivery, back_from_orden_kosmo
from Imperium import imperium_main, adeptus, astra, back_from_astra, back_from_adeptus
import re

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
        callback.data = 'kosmo'
        kosmo_main(callback)

    elif callback.data == 'imperium':
        callback.data = 'imperium'
        imperium_main(callback)

    elif callback.data == 'menu':
        callback.data = 'menu'
        main_menu(callback)

    elif callback.data == 'order':
        callback.data = 'order'
        order(callback)

        @bot.message_handler(content_types=["text"])
        def user_order(message):
            callback.data = 'order'
            if message.text == 'Иванов Иван Иванович, 1665645, https://t.me/ivan': #сделать шаблон через регулярки
                bot.send_message(message.chat.id, 'Заказ создан успешно')
                start(message=message)
            else:
                bot.send_message(message.chat.id, 'Введите текст корректно')
                bot.register_next_step_handler(message, user_order)











    elif callback.data == 'delivery':
        delivery(callback)

    elif callback.data == 'kosmo_units':
        kosmo_units(callback)

    elif callback.data == 'orden_kosmo':
        orden_kosmo(callback)

    elif callback.data == 'back_from_orden_kosmo':
        back_from_orden_kosmo(callback)

    elif callback.data == 'back_from_kosmo_units':
        back_from_kosmo_units(callback)

    elif callback.data == 'adeptus':
        adeptus(callback)

    elif callback.data == 'back_from_adeptus':
        back_from_adeptus(callback)

    elif callback.data == 'astra':
        astra(callback)

    elif callback.data == 'back_from_astra':
        back_from_astra(callback)







bot.infinity_polling()
# bot.polling(none_stop=True, interval=0)