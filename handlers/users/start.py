from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_buttons import Menyu_tugmalari
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
   await message.answer(f"Salom, {message.from_user.full_name}!\n Botga xush kelibsiz",reply_markup=Menyu_tugmalari)

