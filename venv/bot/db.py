import psycopg2
from config import host, user, password, db_name, TOKEN
import telebot
from send_email_message import send_email


bot = telebot.TeleBot(TOKEN)


def main():
    '''Создание базы данных'''

    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f'Server version: {cursor.fetchone()}')


        with connection.cursor() as cursor:
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS users(
                    id serial primary key,
                    first_name varchar(50),
                    user_id int,
                    item_index varchar(255),
                    tg_link varchar(50),
                    vk_link varchar(50),
                    phone_number varchar(50),
                    email varchar(50))'''
            )

            print(f'База данных создана успешно')

    except Exception as e:
        print('main', e)

    finally:
        if connection:
            connection.close()


def connect_to_db(host, user, password, db_name):
    '''Подключение к базе данных'''
    
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )

        connection.autocommit = True

        return connection
    except Exception as e:
        print('connect_to_db', e)


global connect
connect = connect_to_db(host, user, password, db_name)


def add_to_db(message):
    '''Добавление пользователя в базу данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''INSERT INTO users (first_name, user_id) VALUES
                ('{message.from_user.first_name} ', '{message.from_user.id}')'''
            )

    except Exception as e:
        print('add_to_db', e)


def add_to_order(callback, index):
    '''Добавление товара в корзину'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET item_index = CONCAT(item_index, '{index}') WHERE user_id = '{callback.from_user.id}';'''
            )

    except Exception as e:
        print('add_to_order', e)


def select_order(callback):
    '''Показ товара из корзины'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT item_index from users WHERE user_id = {callback.from_user.id}'''
            )

            return ''.join(list(cursor.fetchone()))[:-2]

    except Exception as e:
        print('select_order', e)
        return ''


def delete_user_order(callback):
    '''Удаление всех товаров из корзины'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET item_index = NULL WHERE user_id = '{callback.from_user.id}';'''
            )

    except Exception as e:
        print('delete_user_order', e)


def delete_user(message):
    '''Удаление пользователя из базы данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''DELETE FROM users WHERE user_id = '{message.from_user.id}';'''
            )

    except Exception as e:
        print('delete_user', e)


def check_tg_link(callback):
    '''Проверка, есть ли ссылка на телеграм'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT tg_link FROM users WHERE user_id = '{callback.from_user.id}' AND tg_link IS NOT null;'''
            )

            return cursor.fetchone()

    except Exception as e:
        print('check_tg_link', e)


def add_tg_link(message):
    '''Добавление ссылки на телеграм в базу данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET tg_link = '{message.text}' WHERE user_id = '{message.from_user.id}';'''
            )

    except Exception as e:
        print('add_tg_link', e)


def check_vk_link(callback):
    '''Проверка, есть ли ссылка на вк'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT vk_link FROM users WHERE user_id = '{callback.from_user.id}' AND vk_link IS NOT null;'''
            )

            return cursor.fetchone()

    except Exception as e:
        print('check_vk_link', e)


def add_vk_link(message):
    '''Добавление ссылки на вк в базу данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET vk_link = '{message.text}' WHERE user_id = '{message.from_user.id}';'''
            )

    except Exception as e:
        print('add_vk_link', e)


def check_email(callback):
    '''Проверка, есть ли почта'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT email FROM users WHERE user_id = '{callback.from_user.id}' AND email IS NOT null;'''
            )

            return cursor.fetchone()

    except Exception as e:
        print('check_email', e)


def add_email(message):
    '''Добавление почты в базу данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET email = '{message.text}' WHERE user_id = '{message.from_user.id}';'''
            )

    except Exception as e:
        print('add_email', e)


def check_phone_number(callback):
    '''Проверка, есть ли номер телефона'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT phone_number FROM users WHERE user_id = '{callback.from_user.id}' AND tg_link IS NOT null;'''
            )

            return cursor.fetchone()

    except Exception as e:
        print('check_phone_number', e)

            
def add_phone_number(message):
    '''Добавление телефона в базу данных'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''UPDATE users SET phone_number = '{message.text}' WHERE user_id = '{message.from_user.id}';'''
            )

    except Exception as e:
        print('add_phone_number', e)


def check_order(callback):
    '''Проверка, есть ли товар в корзине'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT item_index FROM users WHERE item_index IS NOT null AND user_id = '{callback.from_user.id}';'''
            )
            return cursor.fetchone()


    except Exception as e:
        print('check_order', e)


def send_order_with_tg(callback):
    '''Отправка готового заказа на почту'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT first_name, item_index, tg_link FROM users WHERE user_id = '{callback.from_user.id}';'''
            )

            order = ''.join(list(cursor.fetchone()))
            send_email(order)

    except Exception as e:
        print('send_order_with_tg', e)


def send_order_with_vk(callback):
    '''Отправка готового заказа на почту'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT first_name, item_index, vk_link FROM users WHERE user_id = '{callback.from_user.id}';'''
            )

            order = ''.join(list(cursor.fetchone()))
            send_email(order)


    except Exception as e:
        print('send_order_with_vk', e)


def send_order_with_email(callback):
    '''Отправка готового заказа на почту'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT first_name, item_index, email FROM users WHERE user_id = '{callback.from_user.id}';'''
            )

            order = ''.join(list(cursor.fetchone()))
            send_email(order)


    except Exception as e:
        print('send_order_with_email', e)


def send_order_with_phone(callback):
    '''Отправка готового заказа на почту'''

    try:

        with connect.cursor() as cursor:
            cursor.execute(
                f'''SELECT first_name, item_index, phone_number FROM users WHERE user_id = '{callback.from_user.id}';'''
            )

            order = ''.join(list(cursor.fetchone()))
            send_email(order)

    except Exception as e:
        print('send_order_with_phone', e)


if __name__ == '__main__':
    main()