"""
Лекция 5.2.
Инкапсуляция, наследование и полиморфизм
"""


# наследование
# мы создали базовый класс животного, кот содерж почти всю функциональность кота

# полиморфизмом
# мы изменяем поведение с учетом особенности текущего класса,
# но его использование никак не измен: не возник новые парметры, особенности, неожид ситуации

class Animal():
    _count = 0

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


# чтобы кот наследовался о животконо и брал все его методы и поля при создании класса в скобках указываем базовый класс (Animal)
class Cat(Animal):

    # когда происходит наследование, мы можем переопределить часть поведения, чтобы сделать логику более подходящую для этой ситуации
    # можно переопредел методы и свойства, но переопредел методы должны рабоать похожим образом и сильно не изменять логику!
    # переопредел метод должен работать предсказуемо в этой иерархии классов

    # переопределяем метод из базового класса
    def __str__(self):
        # мы не можем напрямую работать с приватным свойством __name в классе-наследнике
        # return f'Кот {self.__name}'
        return f'Кот {self.get_name()}'

    # мы переопределили этот метод он не стал сложнее, не появились доп параметры,
    # вызывается и работает точно так же как и у животного, но с учетом особенности кота
    # этот принцип и называется полиморфизмом
    # мы изменяем поведение с учетом особенности текущего класса,
    # но его использование никак не измен: не возник новые парметры, особенности, неожид ситуации
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

parrot = Animal("Кеша", 3, "red")
print(parrot)
parrot.say()



class Device():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# и телефон, и камера одинаковым образом могут делать фото
# значит если мы посто хотим сделать фото, то нам не важно какой объект использовать
class Phone(Device):
    def make_a_call(self, phone_number):
        print(f"Звоним на {phone_number}")

    def take_a_photo(self):
        print(f"{self.name}: фотография!")


class PhotoCamera(Device):
    def take_video(self):
        print('записывает видео')

    def take_a_photo(self):
        print(f"{self.name}: фотография!")


objs = [Phone("samsung"), PhotoCamera("canon")]
for obj in objs:
    obj.take_a_photo()

# это и есть полиморфизм, оба устройства делают фото
# есть какое-то одинк поведение, кот работает одинак для любого объекта, кот умеет этим заниматься
# и мы можем выбрать любой из них, чтобы решить нашу задачу
# те у них есть одинак интерфейс и мы можем его исп чтобы решить нашу задачу
