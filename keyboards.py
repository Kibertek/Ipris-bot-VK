from vkbottle import Keyboard, Text


def main_menu():
    keyboard = Keyboard(one_time=False, inline=False)

    keyboard.add(Text("📍 Филиал №1", payload={"branch": "1"}))
    keyboard.row()

    keyboard.add(Text("📍 Филиал №2", payload={"branch": "2"}))
    keyboard.row()

    keyboard.add(Text("📍 Филиал №3", payload={"branch": "3"}))
    keyboard.row()

    keyboard.add(Text("📍 Филиал №4", payload={"branch": "4"}))

    return keyboard.get_json()


def services_menu():
    keyboard = Keyboard(one_time=False, inline=False)

    keyboard.add(Text("📄 Печать документов"))
    keyboard.row()

    keyboard.add(Text("🖼️ Широкоформатная печать"))
    keyboard.row()

    keyboard.add(Text("💳 Визитки"))
    keyboard.row()

    keyboard.add(Text("📷 Фото"))
    keyboard.row()

    keyboard.add(Text("👕 Печать на одежде"))
    keyboard.row()

    keyboard.add(Text("🎁 Сувенирная продукция"))
    keyboard.row()

    keyboard.add(Text("📚 Брошюровка"))
    keyboard.row()

    keyboard.add(Text("✂️ Постпечатная обработка"))
    keyboard.row()

    keyboard.add(Text("❓ Другое"))

    return keyboard.get_json()
