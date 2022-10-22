"""
Лекция 2.2.
Подключение системных модулей.
Модуль os - работа с файлами и каталогами
"""

import os  # импортируем модуль для работы с операционными системами
from os import path  # обращаемся напрямую к path, а не через os.path
from pathlib import Path # класс для взаимодействия с путями

cur_path = os.getcwd()  # путь до текущей папки (папки проекта)
print(cur_path)
file_dir = os.path.join(cur_path, "files") # join соедин различные части путей и дает соединенный путь, теперь в папке проекта появится папка для файлов
print(file_dir)
# os.mkdir(file_dir) # создаем эту папку, но это можно сделать только 1 раз, так как папка уже будет существовать или обрабатываем исключение
try:
    os.mkdir(file_dir)
except FileExistsError:
    pass  # ключевое слово, обознач пустой блок кода

# в коде нельзя писать вручную конкретные пути, так как в другой ос они не откроются!

file_path = os.path.join(file_dir, 'file6.txt')

with open(file_path, "a+", encoding="utf-8") as file:
    file.write("123")
    file.seek(0)
    print(file.read())

#os.remove("file.txt")  # удаляем файл
print(os.path.exists("file.txt"))  # проверяем существование файла

print(file_path)
print(path.basename(file_path))  # название файла
print(path.dirname(file_path))   # путь к папке, в которой находится файл
print(path.splitext("file.txt"))  # имя и расширение файла

# обращаемся к фйлам и папкам, которые находятся на уровень выше (родительским)
print(path.join("..", "testdir"))   # относительный путь (относ папки в кот мы находимся)
print(path.abspath(path.join("..", "testdir")))  # превращ относит путь в абсолютный путь


# pathlib and Path
cur_path = os.getcwd()
file_dir = Path(cur_path) / "files" # / вместо join
print(file_dir)
try:
    file_dir.mkdir()
except FileExistsError:
    pass  # ключевое слово, обознач пустой блок кода

# в коде нельзя писать вручную конкретные пути, так как в другой ос они не откроются!

file_path = file_dir / 'file.txt'

with file_path.open("a+", encoding="utf-8") as file:
    file.write("123")
    file.seek(0)
    print(file.read())

#os.remove("file.txt")  # удаляем файл
print(Path("file.txt").exists())  # проверяем существование файла

# переменная окружения CAPS LOCK (так как это константы, в пиноне они капсом)
# path (при установке программ) - это спец переменная окружения, в которой храниться список папок с программами
# механизм этих переменных удобен для настройки программ

print(os.environ.get("TEST"))  # None, TEST - переменная окружения, хотим найти значение этой перем
# если перед запуском указать значение переменной (с переменной окружения), то будет оно, иначе знач по умолчанию
print(os.environ.get("TEST", "default value for environment variable"))  # добавили значение по умолчанию

TEST = os.environ.get(
    "TEST",
    "default value for environment variable"
)
print("test:", TEST)