import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import MySQLConnection
import sys

from aiogram.dispatcher.filters import Text

from datetime import datetime
import pytz

import os
import sys
from os import getenv
# from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
# from pathlib import Path

import keyboards.keyboards as kb
from keyboards.message_texts import *
# from src.api import app
from utils.database import *


# load_dotenv('./docker/envs/.env')

# API_TOKEN = os.getenv('api_token')
# TODO: fix it
app.config.from_object("config.Config")
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# DB CONNECT
try:
    db = connect("events_data")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("There is something wrong with your username or password")
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
        sys.exit()
    else:
        print(err)
        sys.exit()

cursor = db.cursor()

# Create a base if not.
# cursor.execute("CREATE DATABASE IF NOT EXISTS a0549853_td_bd")

# Create a table if not.
cursor.execute("CREATE TABLE IF NOT EXISTS visitors (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, user_name VARCHAR(255), user_first_name VARCHAR(255), user_last_name VARCHAR(255), date_time DATE, user_phone_number VARCHAR(20))")
cursor.execute("CREATE TABLE IF NOT EXISTS visitors_need_help (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, user_full_name VARCHAR(255), user_phone_number VARCHAR(20), date_time DATE, status BOOLEAN)")
db.commit()
# /DB CONNECT

utc_dt = pytz.utc.localize(datetime.utcnow())
kiev_tz = pytz.timezone('Europe/Kiev')
DATE_TIME = utc_dt.astimezone(kiev_tz)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    if not visitor_exists(cursor, message.from_user.id):
        add_visitor(db, cursor, message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, DATE_TIME)
    await bot.send_message(message.from_user.id, start_hello_text, reply_markup=kb.markup_main)


@dp.message_handler(commands=['events'])
async def send_events(message: types.Message):
    await bot.send_message(message.from_user.id, chose_events_text, reply_markup=kb.markup3)


@dp.message_handler(Text(equals='Events'))
async def send_events(message: types.Message):
    await bot.send_message(message.from_user.id, chose_events_text, reply_markup=kb.markup3)


@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id, help_text, reply_markup=kb.btn_request_contact)


@dp.message_handler(Text(equals='Help'))
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id, help_text, reply_markup=kb.btn_request_contact)


# Get phone number from Contact --> save to DB
@dp.message_handler(content_types=["contact"])
async def test(message: types.Message):
    if visitor_exists(cursor, message.from_user.id):
        add_visitor_phone_number(db, cursor, message.from_user.id, message.contact.phone_number)
    else:
        add_visitor(db, cursor, message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, DATE_TIME)
    add_visitor_need_help(db, cursor, message.from_user.id, message.from_user.full_name, message.contact.phone_number, DATE_TIME, status=False)
    text = f"{message.from_user.full_name} {thank_for_number_text}"
    await message.answer(text)


# @dp.message_handler()
# async def process_help(message: types.Message):
#     await message.reply("Don't understand 🤯")


# Subscription activation command TODO!!!
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # if the user is not in the database, add him
        db.add_subscriber(message.from_user.id)
    else:
        # if it already exists, then simply update the subscription status for it
        db.update_subscription(message.from_user.id, True)

    await message.answer(subscribe_text)


# Unsubscribe command TODO!!!
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # if the user is not in the database, add him with an inactive subscription (remember)
        db.add_subscriber(message.from_user.id, False)
        await message.answer(unsubscribe_text_1)
    else:
        # if it already exists, then simply update the subscription status for it
        db.update_subscription(message.from_user.id, False)
        await message.answer(unsubscribe_text_2)


# TODO:
# 1. Set main menu.
# 2. Set inline buttons for Events, Courses etc.
# 3. Add site-url.
# 4. Implement MySQL or PostgresDB
# 5. Deploy bot to hosting


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
