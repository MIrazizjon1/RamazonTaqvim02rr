from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from keyboards.inline.sahar_iftor import Ta
from keyboards.inline.sana_buttons import sanalar
from loader import dp, bot


# Echo bot
@dp.message_handler(text="🗓 To'liq taqvim")
async def bot_echo(message: types.Message):
    await message.answer(text="Quyidagi sanalardan birini tanlang:",reply_markup=sanalar)

@dp.callback_query_handler(text="s1")
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="Quyidagilardan birini tanlang:\n",reply_markup=Ta)

@dp.callback_query_handler(text='t1')
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    rasm_manzil = InputFile(path_or_bytesio='C:/Users/user/Downloads/ramadan-800-txt.jpg')
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,
                         caption="Saharlik vaqti  ---  4:37")
#                   Iftorlik

@dp.callback_query_handler(text="s1")
async def bot_echo(message: CallbackQuery):
    await message.message.answer(text="Quyidagilardan birini tanlang:\n",reply_markup=Ta)

@dp.callback_query_handler(text='t2')
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    rasm_manzil = InputFile(path_or_bytesio='C:/Users/user/Downloads/ramadan-800-txt.jpg')
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,
                         caption="Iftorlik vaqti  ---  18:47")
