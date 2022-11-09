"""
Написать ĸонсольную программу, ĸоторая принимает IP и возвращает страну, с
помощью API https://ip-api.com/docs/api:json
Если IP не существует, нужно вывести ошибĸу "Таĸого IP не существует".
"""
import requests

api = "http://ip-api.com/json/"
ip = input("Введите IP \n")
link = api + ip
response = (requests.get(link)).json()
print(response)

if response['status'] == 'success':
    print(response['country'])
else:
    print("Таĸого IP не существует")