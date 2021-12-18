from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .keyboards_name import *

btn_events = KeyboardButton(btn_events_name)
btn_courses = KeyboardButton(btn_courses_name)
btn_certification = KeyboardButton(btn_certification_name)
btn_site = KeyboardButton(btn_site_name)
btn_help = KeyboardButton(btn_help_name)
markup_main = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_events, btn_courses, btn_certification)
markup_main.add(btn_site, btn_help)
# markup1 = ReplyKeyboardMarkup().row(events_kb)

btn_event_1 = KeyboardButton(btn_event_1_name)
btn_event_2 = KeyboardButton(btn_event_2_name)
btn_event_3 = KeyboardButton(btn_event_3_name)
# markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(event_1).add(event_2).add(event_3)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_event_1, btn_event_2, btn_event_3)

markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_event_1, btn_event_2, btn_event_3).add(
    KeyboardButton("Site"))

btn_request_contact = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(btn_request_contact_name, request_contact=True))

# markup3.row(KeyboardButton("5"), KeyboardButton("6"))
# markup3.insert(KeyboardButton("7"))
# markup3.add(KeyboardButton("New line"))
