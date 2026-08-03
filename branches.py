"""
branches.py

Информация о филиалах ИПРИС.
"""

BRANCHES = {
    "1": {
        "name": "Филиал №1",
        "address": "Адрес филиала №1",
        "phone": "+7 (000) 000-00-01",
        "email": "office1@ipris.ru",
        "work_time": "Пн–Пт: 09:00–20:00"
    },

    "2": {
        "name": "Филиал №2",
        "address": "Адрес филиала №2",
        "phone": "+7 (000) 000-00-02",
        "email": "office2@ipris.ru",
        "work_time": "Пн–Пт: 09:00–20:00"
    },

    "3": {
        "name": "Филиал №3",
        "address": "Адрес филиала №3",
        "phone": "+7 (000) 000-00-03",
        "email": "office3@ipris.ru",
        "work_time": "Пн–Пт: 09:00–20:00"
    },

    "4": {
        "name": "Филиал №4",
        "address": "Адрес филиала №4",
        "phone": "+7 (000) 000-00-04",
        "email": "office4@ipris.ru",
        "work_time": "Пн–Пт: 09:00–20:00"
    }
}


def get_branch(branch_id: str):
    """
    Возвращает информацию о филиале по его ID.
    """
    return BRANCHES.get(branch_id)


def get_email(branch_id: str):
    """
    Возвращает email филиала.
    """
    branch = get_branch(branch_id)
    return branch["email"] if branch else None


def get_phone(branch_id: str):
    """
    Возвращает телефон филиала.
    """
    branch = get_branch(branch_id)
    return branch["phone"] if branch else None


def get_address(branch_id: str):
    """
    Возвращает адрес филиала.
    """
    branch = get_branch(branch_id)
    return branch["address"] if branch else None


def get_work_time(branch_id: str):
    """
    Возвращает время работы филиала.
    """
    branch = get_branch(branch_id)
    return branch["work_time"] if branch else None
