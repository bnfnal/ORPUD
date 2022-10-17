"""
Лекция 1.5.
Работа с циклами.
Функция range
"""

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("-" * 10)

# цикл по элементам списка
for item in lst2:  # элементы списка сразу хранятся в памяти
    print(item)

print(range(10))  # числа от 0 до 9
print(list(range(10)))

for i in range(10):  # не занимает места в памяти, range(10) не генерирует список при обращении к нему, постепенно выдает следующие элементы (генерируются в ходе выполнения цикла)
    print(i)

for i in range(10):
    if i == 5:
        continue  # пропускаем итерацию
    if i == 9:
        break  # останавливаем (прерываем) работу цикла
    print(i)

cats = ["Барсик", "Мурзик", "Василий"]
print(list(enumerate(cats)))  # функция enumerate() возвращает список с парами, где первый эл-т - индекс, второй - значение

for idx, cat in enumerate(cats):
    print(f"{idx}. {cat}")

print(list(reversed(cats)))  # разворачивет список, reversed() содержит спец оператор
print(list(reversed(cats)))  # сортирует список по алфавиту


eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

for key, value in eng_rus_dict.items():
    print("ключ -", key, "значение -", value)

i = 0
while i != 5:
    i += 1
print(i)

# выводим алфавит
print("а", ord("а"))  # ord() выводит код символа
symbol_number = ord("а")
while symbol_number <= ord("я"):
    print(symbol_number, chr(symbol_number))  # chr() выводит буквенное представление символа по его номеру
    symbol_number += 1

