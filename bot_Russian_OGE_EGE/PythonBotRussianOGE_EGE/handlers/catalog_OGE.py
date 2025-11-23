from aiogram import F, Router, types
from aiogram.filters import Command, BaseFilter

from keyboards.OGE import generate_OGE_menu_kb

import random

FLAG = False
ANSWER = ''

router = Router()


@router.callback_query(F.data == 'OGE')
@router.message(F.text == 'Подготовка к ОГЭ')
async def OGE_study(update: types.Message | types.CallbackQuery):
    if isinstance(update, types.Message):
        await update.answer(
            'Выберите задание:',
            reply_markup=generate_OGE_menu_kb()
        )
    else:
        await update.message.edit_text(
            'Выберите задание:',
            reply_markup=generate_OGE_menu_kb()
        )



@router.callback_query(F.data.startswith('OGE_task'))
async def OGE_task_info(callback: types.CallbackQuery):
    task_num = callback.data.split(':')[-1]

    path = f'data/OGE/task{task_num}/'
    theory_path = path + f'task_{task_num}_theory.pdf'

    await callback.message.answer_document(types.FSInputFile(theory_path))

    await callback.message.answer(
        'Хотите решить задание?',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Да', callback_data=f'YES:{task_num}'),
                 types.InlineKeyboardButton(text='Нет', callback_data='OGE'),
                ]
            ]
        )
    )


@router.callback_query(F.data.startswith('YES'))
async def give_task(callback: types.CallbackQuery):
    global FLAG, ANSWER
    FLAG = True
    task_num = callback.data.split(':')[-1]
    path = f'data/OGE/task{task_num}/'
    file = open(path + f'{random.randint(1,20)}.txt', encoding='UTF-8')
    text, ANSWER = file.read().split('Ответ:')
    ANSWER = ANSWER.strip(' .!?-+\n')

    await callback.message.answer(text)

@router.message(lambda message: FLAG)
async def check_answer(message: types.Message):
    user_answer = message.text
    print(f'cor.: {ANSWER}')
    print(f'user: {user_answer}')
    if user_answer == ANSWER:
        await message.answer('Молодец')
    else:
        await message.answer('Неверно')


