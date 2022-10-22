"""
Лекция 2.5.
Работа с датой и временем.
Модуль datetime
"""

import datetime # работа с датой и временем
# from datetime import datetime, date, timedelta   # если нужно исп не весь модуль, а только его часть
# после этого названия модуля в коде можно убрать и таким образом сократить код

print(datetime.date.today()) # текущая дата
print(datetime.date.today().strftime(  # преобразует текущую дату в нужный формат
    'today - %d.%m.%Y'
))

print(datetime.datetime.today()) # текущая время
print(datetime.datetime.today().strftime(  # преобразует текущую дату/время в нужный формат
    '%d.%m.%Y %H:%M:%S'   # m - номер месяца, M - кол-во минут
))

# таблица с указанием различных форматов есть в документации python datetime

print(datetime.datetime(2022, 9, 27))  # по умолчанию время = 00:00:00
print(datetime.datetime(2022, 9, 27, 12, 34))

a = datetime.datetime(2022, 9, 27, 12, 34)

print(a.date())  # вытаскиваем день из а
print(a.time())  # вытаскиваем время из а
print(a.strftime('%d.%m.%Y %H:%M:%S' ))   # форматируем вывод а

# чтобы разобрать строчку с датой (на пример, если пользователь ее ввел) в объект с датой
b = datetime.datetime.strptime(
    "27.09.2022 12:34:00",
    "%d.%m.%Y %H:%M:%S"
)
print("дата из strptime", b)

# класс для оперирования с временными промежутками
c = a + datetime.timedelta(hours=1, minutes=30, seconds=1)  # добавляем ко вмемени 1 час 30 мин и 1 сек
print(c)
