"""
Лекция 5.3.
Перегрузка стандартных операций, перегрузка операторов
"""
import random


# пусть животные умеют драться и дерутся они в зависимости от своей силы

class Animal():
    _count = 0
    force = 1   # сила животного

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Animal._count += 1

    def eat(self, fullness=1):
        print(f"{self.__name} поел")
        self.fullness += fullness

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'Животное {self.__name}'

    def say(self):
        print(f'{self.__name} говорит!')

    @staticmethod
    def get_count():
        return Animal._count

    # переопределяем оператор + для драк животных
    def __add__(self, other):
        if self.force > other.force:
            winner_name = self.get_name()
        elif self.force < other.force:
            winner_name = other.get_name()
        else:
            selected = random.choice([self, other])
            winner_name = selected.get_name()
        print('победил', winner_name)


# чтобы кот наследовался о животконо и брал все его методы и поля при создании класса в скобках указываем базовый класс (Animal)
class Cat(Animal):

    force = 2

    def __str__(self):
        return f'Кот {self.get_name()}'

    def say(self):
        print(f'{self.get_name()}: мяу!')

    def mur(self):
        print(f'{self.get_name()}: мур!')


vasya = Cat("Вася", 5, "black")
barsik = Cat("Барсик", 8, "ginger")

print(vasya)
vasya.set_name("Вася Великолепный")
print(vasya.get_name())
print(barsik)

# получение информации об объектах класса, которая записана у них внутри через .
# print(vasya.name, vasya.color)
# print(barsik.name, barsik.color, barsik.fullness)

barsik.eat()
barsik.eat(2)
barsik.eat(3)
print(barsik.fullness)
vasya.say()
vasya.mur()

print(Cat.get_count())
print(vasya + barsik)

parrot = Animal("Кеша", 3, "red")
print(parrot)
parrot.say()
print(parrot + vasya)

