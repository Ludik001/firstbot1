from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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
    await message.answer('Здарва прышь, я твой первый бот Тётя Зина из 5 подъезда и сейчас я скажу кто ты по масте')

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