"""
Лекция 1.4.
Cписок, кортеж, словарь, множество.
Основные методы работы с этими типами переменных
"""

# список
lst = [1, 2, 3]
lst.append(4)
lst.remove(3)

print(lst)

print(lst[0])
print(lst[-1])

lst.remove(2)

if 2 in lst:
    print("2 есть в списке")
else:
    print("2 нет в списке")

lst_console = input("Введите список чисел через пробел: ")
numbers = lst_console.split(" ")
print(numbers)
# в питоне есть функция list(), поэтому называем lst

# кортежи - неизменяемый список, объявляется один раз и в дольнейшем в него нельзя внести изменения (tuple)
tup = (3, 5, 2)
print(tup)
print(tup[0])
print(tup[-1])

first, second, third = tup
print("1", first)
print("2", second)
print("3", third)

print(3 in tup)

# словари, слева - ключ, справа - значение
# по ключу вытаскиваем значение из словаря и можем изменить это значение
eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

print(eng_rus_dict)
print(eng_rus_dict["cat"])
eng_rus_dict["cat"] = "Кошка"
print(eng_rus_dict["cat"])

print("car" in eng_rus_dict)
print(eng_rus_dict.values())
print("кот" in eng_rus_dict.values())
print(eng_rus_dict.keys())
print(eng_rus_dict.items()) # возвращает пары ключ-значения (каждая пара - кортеж)

# print(eng_rus_dict["brother"]) ошибка, так как ключа нет в словаре
print(eng_rus_dict.get("brother", "(нет перевода)"))  # выведет перевод ключа или "(нет перевода)", если ключа нет в словаре

# множества, порядок элементов не важен
# зададим множество с помощью списка
set_from_lst = set(lst)
set_example = {1, 2, 3}
print(set_from_lst)
print(set_example)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
print(set_example.union({6, 7}))
print(set_example == {5, 1, 3})

print(len("брат"))
print(len(lst))
print(len(eng_rus_dict))
print(len(set_example))