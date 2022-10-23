"""
если мы обратимся к модулю translator при импорте, то имеено из этого файла будут происходить подключения
from .console - относительный импорт модулей из папки, в которой находится текущий файл
"""
from .console import print_translation, get_parameters
from .data import REVERSED_DICT, DICT
from .service import get_translation, get_word_translation, prepare_word