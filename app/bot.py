# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import config
import telebot as tgb
from telebot import types
from datetime import datetime
from pathlib import Path
# import model as db
import config
import json
import os
from flask import Flask, request

bot = tgb.TeleBot(config.TOKEN)
#bot = tgb.TeleBot(os.environ['BOT_TOKEN'])
BASE_REF = "https://t.me/tribute/app?startapp=s7HD"

server = Flask(__name__)

# каталоги
BASE_DIR = Path(__file__).resolve().parent
# for local saved
VIDEOS_DIR = BASE_DIR.joinpath('video')
DB_FILE = Path(f'{BASE_DIR}/' + 'mvine.db')


# при выполнении команды start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    video1 = open(f'{VIDEOS_DIR}/video1.mp4', 'rb')
    bot.send_video(message.from_user.id, video1)
    # video2 = open(f'{VIDEOS_DIR}/video2.mp4', 'rb')
    # bot.send_video(message.from_user.id, video2)
    # video3 = open(f'{VIDEOS_DIR}/video3.mp4', 'rb')
    # bot.send_video(message.from_user.id, video3)
    bot.send_message(message.from_user.id, BASE_REF)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("bot starting....")
    bot.infinity_polling()
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    # server.run()
    print("bot stop....")


