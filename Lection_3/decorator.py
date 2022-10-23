"""
Написать деĸторатор, ĸоторый печатает в ĸонсоль ввод и вывод фунĸции. Деĸоратор
должен работать для фунĸций с любыми параметрами. Логиĸа печати в ĸонсоль
должна содержаться именно в деĸораторе, а не в фунĸции, ĸоторую деĸорируете.
"""

def print_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Ввод функции: {args}, {kwargs}")
            print(f"Вывод функции: {func(*args, **kwargs)}")
        except Exception:
            print(Exception)

        return(func(*args, **kwargs))
    return wrapper


@print_decorator
def sentence(*args, **kwargs):
    res = ""
    for word in args:
        res += word + " "
    for word in kwargs.values():
        res += word + " "
    res = res[:-1] + "."
    return res

sentence("Я", "люблю", "программировать на языке", languаge="python")
