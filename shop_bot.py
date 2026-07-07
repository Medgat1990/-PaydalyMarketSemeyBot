import asyncio
import pandas as pd
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

TOKEN = "8557051126:AAFjhByjxGFZJT1fjebF2Pgplh9iow6_kFE"
bot = Bot(token=TOKEN)
dp = Dispatcher()

df = pd.read_excel("Каталог.xlsx")

# Клавиатура
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог")],
        [KeyboardButton(text="📍 Адрес"), KeyboardButton(text="☎️ Контакты")]
    ],
    resize_keyboard=True
)

# Команда /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в Пайдалы Маркет!",
        reply_markup=kb
    )

# Обработка кнопок
@dp.message()
async def menu(message: Message):
    if message.text == "📍 Адрес":
        await message.answer(
            "📍 г. Семей\n"
            "ТД «Жаңа Көктем»\n"
            "Бутик 105/4"
        )

    elif message.text == "☎️ Контакты":
        await message.answer(
            "📞 Телефон: +7 747 440 63 92\n"
            "WhatsApp: +7 747 941 42 58"
        )

    elif message.text == "🛍 Каталог":
        text = "🛍 Каталог товаров:\n\n"

        for _, row in df.iterrows():
            text += (
                f"📦 {row[0]}\n"
                f"💰 {row[1]} ₸\n"
                f"📝 {row[2]}\n\n"
            )

        await message.answer(text)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
