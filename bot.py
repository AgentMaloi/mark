import tracemalloc
import config
import box
import new_bel
import random
import requests
import logging
import asyncio
import pyodbc

from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from bs4 import BeautifulSoup as BS

tracemalloc.start()

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("Случайная цитата волка")
	item2 = types.KeyboardButton("Погода в Беларуси")
	item3 = types.KeyboardButton("Случайный анекдот")
	item4 = types.KeyboardButton("Последние новости")

	markup.add(item1, item2, item3, item4)

	await bot.send_message(message.chat.id, "Привет", parse_mode = 'html', reply_markup = markup)

@dp.message_handler(content_types=['text'])
async def lalala(message: types.Message):
	if message.chat.type == 'private':
		if message.text == 'Случайная цитата волка':
			rand_citata = random.randint(1,10)
			if rand_citata == 1:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_1)
			elif rand_citata == 2:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_2)
			elif rand_citata == 3:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_3)
			elif rand_citata == 4:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_4)
			elif rand_citata == 5:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_5)
			elif rand_citata == 6:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_6)
			elif rand_citata == 7:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_7)
			elif rand_citata == 8:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_8)
			elif rand_citata == 9:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_9)
			elif rand_citata == 10:
				await bot.send_message(message.chat.id, "Случайная циатата волка №" + str(rand_citata))
				await bot.send_message(message.chat.id, config.citata_10)
		elif message.text == 'Погода в Беларуси':
			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton("Брест", callback_data = 'brest')
			item2 = types.InlineKeyboardButton("Минск", callback_data = 'minsk')
			item3 = types.InlineKeyboardButton("Могилёв", callback_data = 'mogilev')
			item4 = types.InlineKeyboardButton("Витебск", callback_data = 'vitebsk')
			item5 = types.InlineKeyboardButton("Гомель", callback_data = 'gomel')
			item6 = types.InlineKeyboardButton("Гродно", callback_data = 'grodno')
			markup.add(item1, item2, item3, item4, item5, item6)
			await bot.send_message(message.chat.id, "Выбирете ваш город", parse_mode = 'html', reply_markup = markup)
		elif message.text == 'Случайный анекдот':
			rand_anekdot = random.randint(1,10)
			if rand_anekdot == 1:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot1)
			elif rand_anekdot == 2:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot2)
			elif rand_anekdot == 3:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot3)
			elif rand_anekdot == 4:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot4)
			elif rand_anekdot == 5:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot5)
			elif rand_anekdot == 6:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot6)
			elif rand_anekdot == 7:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot7)
			elif rand_anekdot == 8:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot8)
			elif rand_anekdot == 9:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot9)
			elif rand_anekdot == 10:
				await bot.send_message(message.chat.id, "Случайный анекдот №" + str(rand_anekdot))
				await bot.send_message(message.chat.id, config.anekdot10)
		elif message.text == 'Последние новости':
			await bot.send_message(message.chat.id, "Последние новости Беларуси")
			await bot.send_message(message.chat.id, new_bel.news_links[0])
		else:
			await bot.send_message(message.chat.id, 'Я не знаю как на это ответить(')

@dp.callback_query_handler(lambda call: True)
async def weateherBel(call:types.CallbackQuery):
	try:
		if call.message:
			if call.data =='brest':
				await bot.send_message(call.message.chat.id, "Брест: " + box.titleBrest[0].text)
			elif call.data =='minsk':
				await bot.send_message(call.message.chat.id, "Минск: " + box.titleMinsk[0].text)
			elif call.data =='mogilev':
				await bot.send_message(call.message.chat.id, "Могилёв: " + box.titleMogilev[0].text)
			elif call.data =='vitebsk':
				await bot.send_message(call.message.chat.id, "Витебск: " + box.titleVitebsk[0].text)
			elif call.data =='gomel':
				await bot.send_message(call.message.chat.id, "Гомель: " + box.titleGomel[0].text)
			elif call.data =='grodno':
				await bot.send_message(call.message.chat.id, "Гродно: " + box.titleGrodno[0].text)

			await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Выбирете ваш город",
				reply_markup = None)

	except Exception as e:
		print(repr(e))

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
