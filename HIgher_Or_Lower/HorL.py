from traceback import print_tb
from logo import logo,vs
import csv
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from requests import *#get()
import os



API_KEY = os.getenv('API_KEY')
dp = Bot(token=API_KEY)
bot = Dispatcher(dp)
kerboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("HIGHER!", "LOWER")


acc = []
with open('highORlow.csv', mode='r') as file:
    all = csv.reader(file)
    for i in all:
        acc.append(i)



def assign():
    a = (random.choice(acc) )
    z = (random.choice(acc) )
    return a, z
a,z=assign()
#print(acc)
print(a)
print(z[3])
def compare(x):
    if x =="high":
        if max(a[3],z[3])==z[3]:
            pass
        else:
            pass
    elif x =="low":
        if max(a[3],z[3])==a[3]:
            pass
        else:
            pass
    else: 
        pass

def play_higher_lower():
	pass




@bot.message_handler(commands=['start', 'Start'])
async def welcome(message: types.Message):
    await message.reply(logo, reply_markup=kerboard_reply)
    await message.reply(f'{a[1]}{z[1]}')


executor.start_polling(bot)