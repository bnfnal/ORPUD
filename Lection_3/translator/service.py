# модуль, функции которого, отвечают за бизнес-логику приложения
# from .data import DICT если запускаем translator, который вне пакета
from data import DICT  # если запускаем main

def get_translation(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return None


def prepare_word(word):
    return word.lower().strip()


def get_word_translation(*args, **kwargs):
    local_dict = dict(**DICT, **kwargs)
    results = []
    for arg in args:
        results.append(get_translation(arg, local_dict))
    return results