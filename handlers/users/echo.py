from aiogram import types
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.Mintaqa_buttons import Davlatlar
from keyboards.inline.sahar_iftor import Taa
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🤲 Duo")
async def bot_echo(message: types.Message):
    await message.answer(text="Quyidagi Duolardan birini tanlang:",reply_markup=Taa)

@dp.callback_query_handler(text='t11')
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    rasm_manzil = InputFile(path_or_bytesio='C:/Users/user/Downloads/Telegram Desktop/saharlik.jpg')
    await bot.send_photo(chat_id=user_id, photo=rasm_manzil,caption="Saharlik (og'iz yopish) duosi")

@dp.callback_query_handler(text='t22')
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    rasm_manzil = InputFile(path_or_bytesio='C:/Users/user/Downloads/Telegram Desktop/iftorlik.jpg')
    await bot.send_photo(chat_id=user_id, photo=rasm_manzil,caption="Iftorlik (og'iz ochish) duosi")

