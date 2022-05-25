from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Ta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Saharlik', callback_data='t1'),
            InlineKeyboardButton(text='Iftorlik', callback_data='t2')
        ]

    ]
)

Taa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Saharlik', callback_data='t11'),
            InlineKeyboardButton(text='Iftorlik', callback_data='t22')
        ]

    ]
)