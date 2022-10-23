"""
Лекция 3.2.
Использование *args, **kwargs
"""

# консольный переводчик
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


def get_parameters():
    word = input("Введите слово для перевода: ")
    print("Выберите направление перевода:")
    print("1 - с английского на русский (по умолчанию)")
    print("2 - с русского на английский")
    direction = input()
    if not direction:
        direction = 1
    direction = int(direction)
    return word, direction


# def - объявление функции, в скобках - параметры функции
def get_translation(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return None

def print_translation(word, translation):
    if translation:
        print(f"Перевод слова {word} - {translation}")
    else:
        print(f"Нет перевода для слова {word}")

def prepare_word(word):
    return word.lower().strip()

# в *args попадает кортеж(tuple) из агрументов функции при вызове,
# в **kwargs попадает словарь из аргументов, заданных с помощью с ключевого слова (key words arguments
# можно явно не объявлять аргументы, они все попадут в tuple или словарь и мы сможем их использовать

def get_word_translation(*args, **kwargs):
    print(args)
    print(kwargs)
    local_dict = dict(**DICT, **kwargs)  # словарь, сост из элементов словарей DICT и kwargs
    lst = [1, 2, 3]
    test_lst = [*args, *lst] # список, объединияющий 2 списка
    print(test_lst)
    results = []
    for arg in args:
        results.append(get_translation(arg, local_dict))
    return results

print(get_word_translation('son', 'mother', 'clock', clock = "часы", key = "ключ"))

"""
while True:
    word, direction = get_parameters()
    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)

    print_translation(word, translation)
"""

# нужно соблюдать порядок!
# простые аргументы, *args, аргументы с ключевыми словами, которые заданы явно (они определяют значение по умолчанию), **kwargs
def test(a, b, *args, is_test = True, **kwargs):
    print("простые аргументы: ", a, b)
    print(args)
    print("is test:", is_test)
    print(kwargs)

test(
    1, 2, 3, 4, 5,
    is_test=False,  # если не задать is_test, то оно автоматически будет True, так как его значение по умолчанию = True
    message = 'вышел зайчик погулять'
)