from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button_1 = KeyboardButton('Отправь фото кисы, а то прокляну тебя')
button_2 = KeyboardButton('Переход на новую клавиатуру')
keyboard.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
button_3 = KeyboardButton('Отправь фото собаки (не меня)')
button_4 = KeyboardButton('Вернуться на прошлую клавиатуру')
keyboard_2.add(button_3, button_4)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для тупыц'),
        types.BotCommand(command='/eat', description='Команда для трапезы'),
        types.BotCommand(command='/unity', description='Команда для скримера')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Здарва прышь, я твой первый бот Тётя Зина из 5 подъезда и сейчас я скажу кто ты по масте', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'Отправь фото кисы, а то прокляну тебя')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://medialeaks.ru/wp-content/uploads/2022/12/photo_2022-12-29_15-50-43-443x500.jpg', caption= 'Вот ваш кот Капитан!')

@dp.message_handler(lambda message: message.text == 'Переход на новую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить Тётю Зину отправить фото будущей шавухи', reply_markup= keyboard_2)

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки (не меня)')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://s0.rbk.ru/v6_top_pics/media/img/4/56/346924588693564.jpeg', caption= 'Вот ваша собака Капитан!')

@dp.message_handler(lambda message: message.text == 'Вернуться на прошлую клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить Тётю Зину отправить фото поющего и вонючего кота', reply_markup= keyboard)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Помощи жди только в шахтах Ебеньграда, сосунок')

@dp.message_handler(commands='eat')
async def eat(message: types.Message):
    await message.reply('Время есть супы из опилок!')

@dp.message_handler(commands='unity')
async def unity(message: types.Message):
    await message.reply('ААААААА, ХОРОРРЫ НА ЮНИТИ!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)