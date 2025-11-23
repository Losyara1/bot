from aiogram import Router, types
from aiogram.filters import Command

from keyboards.menu import main_menu_kb

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}\nЯ бот который поможет подготовиться к русскому языку!',
                         reply_markup=main_menu_kb()
    )

