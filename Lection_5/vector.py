"""
Задача № 5
Реализовать ĸласс Vector(x, y), реализующий операции
сложения
вычитания
умножения на число
"""

class Vector():

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return f'({self.x}, {self.y})'


a = Vector(1, 2)
b = Vector(3, 4)
k = 5
print(a + b)
print(a - b)
print(a * k)