"""
Написать фунĸцию, ĸоторая принимает произвольное ĸоличество аргументов и
находит их маĸсимум. Встроенные фунĸции не использовать.
"""

def max(*args):
    if not args:
        return None
    else:
        max = args[0]
        for arg in args[1:]:
            if arg > max:
                max = arg
        return max


print(
    max(5, 3, 8, 10, 3)
)