import smtplib
import telebot
from telebot import types
from email.mime.text import MIMEText
from config import TOKEN, FROM_EMAIL, TO_EMAIL, PASSWORD
import re

bot = telebot.TeleBot(TOKEN)

def send_email(message):
    sender = FROM_EMAIL
    password = PASSWORD
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Заказ на фигурку'
        server.sendmail(sender, TO_EMAIL, msg.as_string())
    except Exception as e:
        print(e)


