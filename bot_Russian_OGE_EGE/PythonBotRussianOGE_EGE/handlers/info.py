from aiogram import F, Router, types
from aiogram.filters import Command

router = Router()

@router.message(F.text == 'Мой профиль')
async def info(message: types.Message):
    await message.answer(
        (
            f'имя: {message.from_user.full_name}\n'
             'пройдено тем ОГЭ: 0\n'
             'пройдено тем ЕГЭ: 0\n'
             'ожидаемый результат на экзамене: 0'
        )
    )