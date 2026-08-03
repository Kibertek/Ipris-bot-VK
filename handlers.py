from urllib.parse import quote

from vkbottle.bot import BotLabeler, Message

from config import BRANCHES
from keyboards import services_menu

labeler = BotLabeler()

# Здесь хранится выбранный филиал пользователя
# Позже заменим на базу данных
user_branch = {}


@labeler.message(text=[
    "📍 Филиал №1",
    "📍 Филиал №2",
    "📍 Филиал №3",
    "📍 Филиал №4"
])
async def choose_branch(message: Message):

    branch_id = message.text[-1]

    user_branch[message.from_id] = branch_id

    branch = BRANCHES[branch_id]

    await message.answer(
        f"✅ Вы выбрали:\n"
        f"{branch['name']}\n\n"
        "Теперь выберите услугу.",
        keyboard=services_menu()
    )


SERVICES = {
    "📄 Печать документов": "Печать документов",
    "🖼️ Широкоформатная печать": "Широкоформатная печать",
    "💳 Визитки": "Визитки",
    "📷 Фото": "Фото",
    "👕 Печать на одежде": "Печать на одежде",
    "🎁 Сувенирная продукция": "Сувенирная продукция",
    "📚 Брошюровка": "Брошюровка",
    "✂️ Постпечатная обработка": "Постпечатная обработка",
    "❓ Другое": "Другое"
}


@labeler.message(text=list(SERVICES.keys()))
async def choose_service(message: Message):

    if message.from_id not in user_branch:
        await message.answer(
            "Сначала выберите филиал."
        )
        return

    branch = BRANCHES[user_branch[message.from_id]]
    service = SERVICES[message.text]

    subject = quote(f"Заказ через VK | {service}")

    body = quote(
        f"""Здравствуйте!

Хочу оформить заказ.

Филиал:
{branch['name']}

Услуга:
{service}

Файлы прикреплены.

Спасибо!"""
    )

    mailto = f"mailto:{branch['email']}?subject={subject}&body={body}"

    await message.answer(
        f"📧 Ваш заказ почти готов.\n\n"
        f"Филиал: {branch['name']}\n"
        f"Почта: {branch['email']}\n\n"
        f"Нажмите на ссылку ниже, откройте письмо, прикрепите файлы и отправьте.\n\n"
        f"{mailto}"
    )
