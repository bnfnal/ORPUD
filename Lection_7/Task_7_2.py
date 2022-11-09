"""
Написать ĸонсольную программу, ĸоторая выводит погоду с сайта
https://yandex.ru/pogoda на сегодня и на неделю.
"""

import requests
import bs4

response = requests.get('https://yandex.ru/pogoda/')

tree = bs4.BeautifulSoup(response.text, 'html.parser')

weather = list()

for item in tree.select('.forecast-briefly'):

    for day in item.select('.forecast-briefly__name')[1:8]:
        weather.append(day.text)

    weather[0] += (' (' + item.select('.forecast-briefly__date')[1].text + ') ' +
                   " днем " + item.select('.forecast-briefly__temp')[2].text[4:] +
                   ", ночью " + item.select('.forecast-briefly__temp')[3].text[5:] +
                   "  " + item.select('.forecast-briefly__condition')[1].text
                   )
    for i in range(2, 8):
        weather[i-1] += (' (' + item.select('.forecast-briefly__date')[i].text + ') ' +
                       " днем " + item.select('.forecast-briefly__temp')[2 * i].text +
                       ", ночью " + item.select('.forecast-briefly__temp')[2 * i + 1].text +
                       "  " + item.select('.forecast-briefly__condition')[i].text
                       )


    print('Прогноз погоды на сегодняшний день с сайта https://yandex.ru/pogoda: ')
    print(weather[0])
    print()

    print('Прогноз погоды на неделю с сайта https://yandex.ru/pogoda: ')
    for i in weather:
        print(i)
