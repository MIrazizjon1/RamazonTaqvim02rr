from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Menyu_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ Bugun")
        ],[
            KeyboardButton(text="⌛ Ertaga"),
            KeyboardButton(text="🗓 To'liq taqvim")
        ],[
            KeyboardButton(text="🇺🇿 Mintaqa"),
            KeyboardButton(text="🤲 Duo")

        ]
    ],resize_keyboard=True
)