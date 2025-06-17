from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_staff_management_menu():
    """
    Возвращает reply-клавиатуру с меню управления персоналом для администратора.

    Предоставляет доступ к следующим действиям:
    - Добавить кассира
    - Удалить кассира
    - Посмотреть список кассиров
    - Вернуться в главное меню

    Returns:
        ReplyKeyboardMarkup: Клавиатура с кнопками:
            - ➕ Добавить кассира
            - ➖ Удалить кассира
            - 📋 Список кассиров
            - ◀️ Главное меню
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text="➕ Добавить кассира")
    builder.button(text="➖ Удалить кассира")
    builder.button(text="📋 Список кассиров")
    builder.button(text="◀️ Главное меню")
    builder.adjust(2, 1, 1)
    return builder.as_markup(resize_keyboard=True)


def get_staff_main_menu():
    """
    Возвращает reply-клавиатуру главного меню администратора.

    Предоставляет доступ к следующим действиям:
    - Управление персоналом (добавление/удаление кассиров)
    - Рассылка сообщений клиентам
    - Просмотр статистики (в разработке)

    Returns:
        ReplyKeyboardMarkup: Клавиатура с кнопками:
            - 👥 Управление персоналом
            - 📢 Рассылка
            - 📊 Статистика
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text="👥 Управление персоналом")
    builder.button(text="📢 Рассылка")
    builder.button(text="📊 Статистика")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)

