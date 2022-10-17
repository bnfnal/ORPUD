"""
Лекция 1.3.
Условный оператор. Формирование блоков кода
"""

name = input("Введите имя: ")
age = float(input("Введите возраст: "))
is_working_now = (input("Работает сейчас? (1 или 0)")) == "1"

print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Работает сейчас: {is_working_now}")

"""
workplace = "КФУ"
if is_working_now:
    print("Место работы: " + workplace)
"""
workplace = None #значение, которое не значит ничего (аналог null)
if is_working_now:
    workplace = input("Место работы:")

"""
if is_working_now and workplace == "":
    print("не заполнено место работы!")
    
if workplace == "":
    print("не заполнено место работы!")
    
if workplace == "" or workplace is None:
    print("не заполнено место работы!")
"""

if is_working_now and not workplace:
    print("не заполнено место работы!")  # сообщение появляется только если человек где-то работает и 

if age >= 18:
    print("совершеннолетний")
else:
    print("несовершеннолетний")

# чтобы проверить несколько условий
if age != 20:
    print("Пользователю не 20 лет")
elif age >= 18:
    print("совершеннолетний")
else:
    print("несовершеннолетний")


