"""
Лекция 6.2.
Использование регулярных выражений в Python: поиск и замена строк
"""

# этот модуль помогает работать с регулярными выражениями в python
import re

# перенесем наши регулярные выражения в python

text = ("Добрый вечер! Меня зовут Василий, моя электронная "
        "почта va-sya_1990@yandex.ry, моя рабочая почта "
        "Vasya@company-2020.com."
        )

# первый аргумент re.search - паттерн, он должен начинаться с r""
# второй арг - текст, в кот будет производиться поиск
# третьим - модификаторы, вводи их через re.
# g (global) будет продолжать искать след совпадения после нахождения первого (он идет по умолчанию в python)
# m (multi line) поиск не останавл на первой строке, а продолжает дальше по всем строкам

result = re.search(r"[\w\d_-]+@[\w\-_\d]+\.\w+", text, re.MULTILINE)
print(result)  # появился объект re.Match, кот на определенных позициях нашел первую почту из текста
print(result.string)  # возвращает исходный текст
print(result.group(0))  # содержимое того, что было найдено

# если мы хотим найти все совпадения исп метод re.finditer, кот вернет итератор,
# те объект кот можно будет перебрать в цикле и вытащить все совпадения из этой строчки
result = re.finditer(r"[\w\d_-]+@[\w\-_\d]+\.\w+", text, re.MULTILINE)
for item in result:
    print(item.group(0))  # вытаскиваем нулевые группы из всех совпадений
# таким образом находим все совпадения


text = "09/23/2022"
# если ходим что-то заменить исп фуункцию re.sub:
# первый аргумент - паттерн, он должен начинаться с r"" - регул выражения, с помощью кот будет искать нужную подсттроку
# второй арг - шаблон начинающийся с r"", с помощью кот будет показана итоговая строка (после измен подстроки), указ порядок групп
# в нашем случае порядок групп r"\2/\1/\3" (номер группы через \, между группами /), группы указываются в порядке расплоложения ()
# третьим - текст, в кот нужно производить земену
result = re.sub(r"([0-3]\d)/(\d{2})/(\d{4})", r"\2/\1/\3", text)
print(result)

# выводим разные группы (вытаскиваем элементы регулярного выражения), чтобы их можно было использовать далее в коде поотдельности
result2 = re.search(r"([0-3]\d)/(\d{2})/(\d{4})", text)
print("month", result2.group(1))
print("day", result2.group(2))
print("year", result2.group(3))

# на regex101.com можно посмотреть на код, кот генерируется сервисом
# при нажатии на кнопку 'Code Generator' мы можем на разных языках программирования сгенерировать код,
# который будет использовать введенное нами регулярное выражение и текст
# код показывает примеры для работы с различными элементами регулярного выражения

"""
([0-3]\d)/(\d{2})/(\d{4})

09/23/2022
01
31
"""

"""
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"([0-3]\d)/(\d{2})/(\d{4})"

test_str = ("09/23/2022\n"
	"01\n"
	"31")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    # match.groups() - итерация по группам
    for groupNum in range(0, len(match.groups())):  
        groupNum = groupNum + 1  
        
        # match.group(groupNum) - вытаскиваются разные элементы групп
        print ("Group {groupNum} found at {start}-{end}: {group}".format(
        groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum))
        )

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
"""


