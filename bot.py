import knopki as kb
from config import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType, InputFile
from aiogram.dispatcher.filters import Command

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def main(message: types.Message):
  await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=kb.menu_kb)

@dp.message_handler(text='🛒Магазин')
async def main(message: types.Message):
	await bot.send_message(message.from_user.id, '🛒Магазин:', reply_markup=kb.menu_Tovar.inline_kb_back)
	await bot.send_message(message.from_user.id, '',  reply_markup=kb.inline_kb_back)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)