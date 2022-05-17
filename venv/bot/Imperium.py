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
    Astra = types.InlineKeyboardButton(text='Астра милитарум (имперская гвардия)', callback_data='astra')
    Adeptus = types.InlineKeyboardButton(text='Адептус механикус', callback_data='adeptus')
    menu = types.InlineKeyboardButton(text='Назад в главное меню', callback_data='menu')
    imperium_inline.add(Astra, Adeptus, menu)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/imperium.png', 'rb'), caption=IMPERIUM_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=imperium_inline)


def astra(callback):
    astra_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='back_from_astra')
    astra_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/astra.png', 'rb'), caption=ASTRA_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=astra_inline)

def back_from_astra(callback):
    imperium_main(callback)



def adeptus(callback):
    adeptus_inline = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton(text='Назад', callback_data='back_from_adeptus')
    adeptus_inline.add(back)
    bot.edit_message_media(
        media=types.InputMedia(media=open('pictures/adeptus.png', 'rb'), caption=ADEPTUS_TEXT, type="photo"),
        chat_id=callback.message.chat.id, message_id=callback.message.id,
        reply_markup=adeptus_inline)


def back_from_adeptus(callback):
    imperium_main(callback)



