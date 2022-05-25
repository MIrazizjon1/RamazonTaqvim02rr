from aiogram import types
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.Mintaqa_buttons import Davlatlar
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🇺🇿 Mintaqa")
async def bot_echo(message: types.Message):
    await message.answer(text="Quyidagi Mamlakatlardan birini tanlang:",reply_markup=Davlatlar)
