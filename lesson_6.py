# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):

        i = 0
        print(f'Светофор переключается на')
        while i < 3:
            if i == 0:
                print(f'{TrafficLight.__color[i]} свет')
                time.sleep(7)
            elif i == 1:
                print(f'{TrafficLight.__color[i]} свет')
                time.sleep(2)
            elif i == 2:
                print(f'{TrafficLight.__color[i]} свет')
                time.sleep(7)
            i += 1

svetofor = TrafficLight()
svetofor.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
    _length = None
    _width = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asphalt(self):
        result = self.length * self.width * 0.25 * 0.05
        print(result, 'тонн')

raschet = Road(5000, 20)
raschet.asphalt()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    wage = None
    bonus = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_profit(self):
        self.__income = {'Доход': self.wage, 'Премия': self.bonus}
        return self.__income

personal = Position('Иван', 'Иванов', 'Продавец', 25000, 5000)
print(personal.get_full_name(), personal.get_full_profit())


# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
        if self.speed > 40:
            print('Превышение скорости')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print('Это полицейская машина')

bmw = PoliceCar(180, 'Белый', 'BMW', True)
bmw.go()
bmw.turn('налево')
bmw.stop()
bmw.show_speed()
bmw.police()
print(bmw.name, bmw.color)

taxi = WorkCar(65, 'Желтый', 'Hundai', False)
print(taxi.name, taxi.color)
taxi.show_speed()
taxi.go()
taxi.turn('направо')
taxi.stop()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

s = Stationery(None)
s.draw()

p = Pen('ручкой')
p.draw()

pe = Pencil('карандашом')
pe.draw()

h = Handle('маркером')
h.draw()
