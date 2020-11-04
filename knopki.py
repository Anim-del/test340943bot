from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Меню бота
buttonProfile = KeyboardButton('️👤Профиль')
buttonShop = KeyboardButton('🛒Магазин')
buttonReviews = KeyboardButton('📗Отзывы')
buttonСontact = KeyboardButton('📞Контакты')
buttonReplenishment = KeyboardButton('💸Пополнение')

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(buttonShop).insert(buttonProfile).insert(buttonСontact).insert(buttonReplenishment).insert(buttonReviews)
#Меню бота


#Кнопка назад
buttonBack = KeyboardButton('🔙 В главное меню')

inline_kb_back = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(buttonBack)
#Кнопка назад



#Товарка
buttonTovar = InlineKeyboardButton('Товар', callback_data='tovar')

menu_Tovar = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(buttonTovar)
#Товарка