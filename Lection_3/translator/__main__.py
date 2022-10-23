# этот файл нужен, чтобы можно было запускать программу не из файла translator, а сразу запускать весь модуль translator из консоли
# если при этом файл translator будет находиться вне папки, наш  импорт с помощью init перестанет работать и в него нужно будет вернуть обычные импорты
# копируем содержимое файла траслятор translator
# здесь относительные импорты через . работать НЕ будут, используем абсолютные импорты из нашего пакета (он будет корнем)

from console import print_translation, get_parameters
from data import REVERSED_DICT, DICT
from service import get_translation, get_word_translation, prepare_word

while True:
    word, direction = get_parameters()
    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)

    print_translation(word, translation)