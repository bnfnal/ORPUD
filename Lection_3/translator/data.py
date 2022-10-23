# модуль для работы с данными
DICT = {
    "mother": "мама",
    "father": "папа",
    "sun": "солнце",
    "son": "сын",
    "cat": "кот",
    "dog": "собака",
    "car": "машиниа",
    "door": "дверь",
    "note": "заметка",
}

REVERSED_DICT = {}
for key, value in DICT.items():
    REVERSED_DICT[value] = key