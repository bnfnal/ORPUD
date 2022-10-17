"""
Лекция 1.2.
Переменные, типы переменных
"""

name = "Вася"
age = 30.5
is_working_now = True

print("Имя: " + name)
print(f"Имя: {name}")
print("Возраст: " + str(age))
print(f"Возраст: {age}")
print("Работает сейчас: " + str(is_working_now))
print(f"Работает сейчас: {is_working_now}")

# форматированние строк, когда нужно разделить шаблон строки и ее вывод
str_template = "Информация о пользователе: {0} - {1}"
print(str_template.format(name, age))

str_template = "Информация о пользователе: {1} - {0}"
print(str_template.format(name, age))

str_template = "Информация о пользователе: {} - {}"
print(str_template.format(name, age))

print(name.lower())
print(name.upper())
print(name.find("с"))
print(name.replace("я", "ян"))
print(name)

a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(5 // b)  #неполное частное
print(5 % b)  #остаток

number = input("Введите число:") #считываем всегда строки
number = int(number)
print(2*number)

c = 4
c += 1

name = input("Введите имя: ")
age = float(input("Введите возраст: "))
# is_working_now = bool(input("Работает сейчас? (1 или 0)")) при вводе и 1, и 0 будет выводиться True.
# Так как для питона любая непустая строка = True
is_working_now = (input("Работает сейчас? (1 или 0)")) == "1"

print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Работает сейчас: {is_working_now}")