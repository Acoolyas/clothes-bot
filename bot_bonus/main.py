import asyncio
import logging
import config
import kb
import sender
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from kb import builder
from bonus import bonus_check

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.BOT_TOKEN)
# Диспетчер
dp = Dispatcher(bot=bot)


# Общие хэндлеры

@dp.message(F.text == "Назад")
async def cmd_contacts(msg: types.Message) -> None:
    global category, category2, size, position
    if position == 'category':
        await msg.answer(f"Добро пожаловать в главное меню", reply_markup=kb.kbmenu.as_markup(resize_keyboard=True))
        position = 'menu'
        category = ''
    elif position == 'category2':
        await msg.answer(f"Выберите товар", reply_markup=kb.kbclothes.as_markup(resize_keyboard=True))
        position = 'category'
        category2 = ''
    elif position == 'size':
        await msg.answer(f"Выберите товар", reply_markup=kb.kbclothes.as_markup(resize_keyboard=True))
        position = 'category2'
        size = ''


# Хэндлер на команду /start

@dp.message(Command("start"))
async def cmd_start(msg: types.Message) -> None:
    global category, category2, size, position
    category = ''
    category2 = ''
    size = ''
    position = 'menu'
    await msg.answer(f"Привет, {msg.from_user.first_name}\nПри возникновении проблем с ботом напишите /start или обратитесь к @callmehustle", reply_markup=kb.kbmenu.as_markup(resize_keyboard=True))
    



# Хэндлеры Главное меню

@dp.message(F.text == "Главное меню")
async def cmd_menu(msg: types.Message) -> None:
    await msg.answer('Добро пожаловать в главное меню', reply_markup=kb.kbmenu.as_markup(resize_keyboard=True))
    global category, category2, size, position
    category = ''
    category2 = ''
    size = ''
    position = 'menu'


@dp.message(F.text == "Одежда")
async def cmd_clothes(msg: types.Message) -> None:
    await msg.answer(f"Выберите товар", reply_markup=kb.kbclothes.as_markup(resize_keyboard=True))
    global category, position
    category = 'clothes'
    position = 'category'

@dp.message(F.text == "Обувь")
async def cmd_shoes(msg: types.Message) -> None:
    # await msg.answer_media_group(media=)
    global category, position
    category = 'shoes'
    category2 = ''
    size = ''
    position = 'menu'
    await sender.Sender(category, category2, size, msg)

@dp.message(F.text == "В пути")
async def cmd_shoes(msg: types.Message) -> None:
    await msg.answer(f'Показаны товары, находящиеся в пути')
    # await msg.answer_media_group(media=)
    global category, position
    category = 'inprocess'
    position = 'menu'
    category2 = ''
    size = ''
    await sender.Sender(category, category2, size, msg)

@dp.message(F.text == "Бонусы")
async def cmd_shoes(msg: types.Message) -> None:
    await msg.answer(bonus_check(msg))
    # await msg.answer_media_group(media=)
    global category, position
    category = 'bonuses'
    position = 'menu'
    category2 = ''
    size = ''

@dp.message(F.text == "Аксессуары")
async def cmd_accs(msg: types.Message) -> None:
    # await msg.answer_media_group(media=)
    global category, position
    category = 'accs'
    category2 = ''
    size = ''
    position = 'menu'
    await sender.Sender(category, category2, size, msg)

@dp.message(F.text == "Контакты")
async def cmd_contacts(msg: types.Message) -> None:
    if position == 'menu':
        await msg.answer(
        'Выберите интересующую Вас площадку',
        reply_markup=builder.as_markup(),
        )

#Хэндлеры категории ниже

@dp.message(F.text == "Толстовки")
async def cmd_hoodies(msg: types.Message) -> None:
    if category == 'clothes':
        await msg.answer(f"Выберите размер", reply_markup=kb.kbsizes.as_markup(resize_keyboard=True))
        global category2, position
        category2 = 'hoodie'
        position = 'category2'



@dp.message(F.text == "Футболки")
async def cmd_tshirts(msg: types.Message) -> None:
    if category == 'clothes':
        await msg.answer(f"Выберите размер", reply_markup=kb.kbsizes.as_markup(resize_keyboard=True))
        global category2, position
        category2 = 'tshirt'
        position = 'category2'


@dp.message(F.text == "Штаны/Шорты")
async def cmd_pants(msg: types.Message) -> None:
    if category == 'clothes':
        await msg.answer(f"Выберите размер", reply_markup=kb.kbsizes.as_markup(resize_keyboard=True))
        global category2, position
        category2 = 'pants'
        position = 'category2'

@dp.message(F.text == "Верхняя одежда")
async def cmd_pants(msg: types.Message) -> None:
    if category == 'clothes':
        await msg.answer(f"Выберите размер", reply_markup=kb.kbsizes.as_markup(resize_keyboard=True))
        global category2, position
        category2 = 'jacket'
        position = 'category2'

#  Хэндлеры размеров

@dp.message(F.text == "XS")
async def cmd_XSsize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'XS'
        await sender.Sender(category, category2, size, msg)


@dp.message(F.text == "S")
async def cmd_Ssize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'S'
        await sender.Sender(category, category2, size, msg)
        # await msg.answer_media_group(media=)

@dp.message(F.text == "M")
async def cmd_Msize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'M'
        await sender.Sender(category, category2, size, msg)
        # await msg.answer_media_group(media=)

@dp.message(F.text == "L")
async def cmd_Lsize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'L'
        await sender.Sender(category, category2, size, msg)
        # await msg.answer_media_group(media=)

@dp.message(F.text == "XL/2XL")
async def cmd_XLsize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'XL/2XL'
        await sender.Sender(category, category2, size, msg)
        # await msg.answer_media_group(media=)

@dp.message(F.text == "Все размеры")
async def cmd_2XLsize(msg: types.Message) -> None:
    if category == 'clothes' and category2 != '':
        global size
        size = 'allsizes'
        await sender.Sender(category, category2, size, msg)
        # await msg.answer_media_group(media=)


# --------------------- main part ------------------------


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())