from vkbottle.bot import Bot, Message
from config import TOKEN
from keyboards import main_menu

# Создаем бота
bot = Bot(token=TOKEN)


@bot.on.message(text=["Начать", "/start", "start"])
async def start_handler(message: Message):
    await message.answer(
        "👋 Добро пожаловать в ИПРИС!\n\n"
        "Выберите филиал, в который хотите отправить заказ.",
        keyboard=main_menu()
    )


@bot.on.message()
async def unknown_handler(message: Message):
    await message.answer(
        "Пожалуйста, воспользуйтесь меню ниже.",
        keyboard=main_menu()
    )


if __name__ == "__main__":
    print("Бот запущен...")
    bot.run_forever()
