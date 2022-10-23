# модуль для работы с консолью

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

def print_translation(word, translation):
    if translation:
        print(f"Перевод слова {word} - {translation}")
    else:
        print(f"Нет перевода для слова {word}")