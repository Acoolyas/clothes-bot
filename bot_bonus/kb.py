from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
back = KeyboardButton(text='Назад')
main_menu = KeyboardButton(text='Главное меню')

kbmenu = ReplyKeyboardBuilder()

kbmenu.row(KeyboardButton(text='Одежда'))
kbmenu.row(KeyboardButton(text='Обувь'))
kbmenu.row(KeyboardButton(text='Аксессуары'))
kbmenu.row(KeyboardButton(text='В пути'), KeyboardButton(text='Контакты'), KeyboardButton(text='Бонусы'))

menu1 = KeyboardButton(text='Одежда')
menu2 = KeyboardButton(text='Обувь')
menu3 = KeyboardButton(text='Аксессуары')
menu4 = KeyboardButton(text='Контакты')

kb_menu = ReplyKeyboardMarkup(keyboard=[[menu1], [menu2], [menu3], [menu4]])

kbclothes = ReplyKeyboardBuilder()

kbclothes.row(
    KeyboardButton(text='Толстовки'),
    KeyboardButton(text='Футболки')
)
kbclothes.row(
    KeyboardButton(text='Штаны/Шорты'),
    KeyboardButton(text='Верхняя одежда')
)
kbclothes.row(KeyboardButton(text='Назад'))
kbclothes.row(KeyboardButton(text='Главное меню'))

clothes1 = KeyboardButton(text='Толстовки')
clothes2 = KeyboardButton(text='Футболки')
clothes3 = KeyboardButton(text='Штаны/Шорты')
clothes4 = KeyboardButton(text='Верхняя одежда')

kb_clothes = ReplyKeyboardMarkup(keyboard=[[clothes1], [clothes2], [clothes3], [clothes4], [back], [main_menu]])

accessories1 = KeyboardButton(text='Нижнее белье')
accessories2 = KeyboardButton(text='Головные уборы')
accessories3 = KeyboardButton(text='Сумки')

kb_accessories = ReplyKeyboardMarkup(keyboard=[[accessories1], [accessories2], [accessories3], [back], [main_menu]])

kbsizes = ReplyKeyboardBuilder()
kbsizes.row(
    KeyboardButton(text='XS'),
    KeyboardButton(text='S'),
    KeyboardButton(text='M')

)
kbsizes.row(
    KeyboardButton(text='L'),
    KeyboardButton(text='XL/2XL'),
    KeyboardButton(text='Все размеры')
)
kbsizes.row(KeyboardButton(text='Назад'))
kbsizes.row(KeyboardButton(text='Главное меню'))

size_s = KeyboardButton(text='S')
size_m = KeyboardButton(text='M')
size_l = KeyboardButton(text='L')
size_xl = KeyboardButton(text='XL')

kb_sizes = ReplyKeyboardMarkup(keyboard=[[size_s], [size_m], [size_l], [size_xl], [back], [main_menu]])

# INLINE KEYBOAD --------------------------


builder = InlineKeyboardBuilder()
builder.row(InlineKeyboardButton(
    text="Telegram", url="https://t.me/hustleseller")
)
builder.row(InlineKeyboardButton(
    text="Avito", url="https://www.avito.ru/user/32a3f0afaea519ac74dc4403b3c469bb/profile?src=sharing")
)
builder.row(InlineKeyboardButton(
    text="VK", url="https://vk.com/hustleseller")
)