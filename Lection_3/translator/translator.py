# главный модуль, в него все импортируется и запускается программа
"""
from Lection_3.translator.console import print_translation, get_parameters
from Lection_3.translator.data import REVERSED_DICT, DICT
from Lection_3.translator.service import get_translation, get_word_translation, prepare_word
для работы с __init.py__ вместо этого импортируем все из самого пакета
но это сработает если этот файл накодится в самом маете либо нет __main__
"""


from Lection_3.translator import(
    print_translation,
    get_parameters,
    REVERSED_DICT,
    DICT,
    get_translation,
    get_word_translation,
    prepare_word
)

while True:
    word, direction = get_parameters()
    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)

    print_translation(word, translation)