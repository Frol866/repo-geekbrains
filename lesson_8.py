# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date():

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def change_int(cls, data):
        day, month, year = map(int, data.split('-'))
        date1 = cls(day, month, year)
        print(f'Тип данных {type(day)}, число {day}')
        print(f'Тип данных {type(month)}, месяц {month}')
        print(f'Тип данных {type(year)}, год {year}')
        return date1

    @staticmethod
    def valid_metod(data):
        day, month, year = map(int, data.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.change_int('16-08-1981')
is_date = Date.valid_metod('16-08-1981')
print(f'Указанная дата {is_date}')


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Division_by_zero(Exception):

    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    @staticmethod
    def func_division(var_1, var_2):
        try:
            return (var_1 / var_2)
        except ValueError:
            return f'Вы ввели не число'
        except:
            return f'ОШИБКА!!! Деление на 0'

var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))

div = Division_by_zero(var_1, var_2)
print(div.func_division(var_1, var_2))

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class Error:

    def __init__(self):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Вы ввели недопустимое значение')
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Выход из программы'

try_except = Error()
print(try_except.my_input())

# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Sklad:

    def __init__(self, name):
        self.name = name
        self.received_lists = {}
        self.transferred_lists = {}

    #метод перемещения на основной склад продукции
    def take_to_sklad(self, equipment):
        self.received_lists.update({equipment.name: equipment.price})
        print(f'На {self.name} принято оборудование {equipment.title} фирмы {equipment.name}, '
              f'цена: {str(equipment.price)}руб. в кол-ве {equipment.number}шт.')

    #метод перемещения товара на точку выдачи
    def moving_to_point(self, equipment):
        self.transferred_lists.update({equipment.name: equipment.price})
        print(f'На {self.name} перемещено оборудование {equipment.title} фирмы {equipment.name}, '
              f'цена: {str(equipment.price)}руб. в кол-ве {equipment.number}шт.')


class Office_equipment:

    def __init__(self, title, name, price, number, *args):
        self.title = title
        self.name = name
        self.price = price
        self.number = number
        self.my_sklad_temp = []
        self.my_sklad = []
        self.input_lists = {}

    def __str__(self):
        return str(self.name)


class Printer(Office_equipment):

    def __init__(self, title, name, price, number, format):
        Office_equipment.__init__(self, title, name, price, number)
        self.format = format

    def __str__(self):
        return  f'{self.title} / Название модели: {Office_equipment.__str__(self)} / Цена: {self.price}руб. / ' \
                f'Кол-во: {self.number}шт. / Формат: {str(self.format)}'


class Xerox(Office_equipment):

    def __init__(self, title, name, price, number, color):
        Office_equipment.__init__(self, title, name, price, number)
        self.color = color

    def __str__(self):
        return  f'{self.title} / Название модели: {Office_equipment.__str__(self)} / Цена: {self.price}руб. / ' \
                f'Кол-во: {self.number}шт. / Цветность: {str(self.color)}'

class Scaner(Office_equipment):

    def __init__(self, title, name, price, number, resolution):
        Office_equipment.__init__(self, title, name, price, number)
        self.resolution = resolution

    def __str__(self):
        return  f'{self.title} / Название модели: {Office_equipment.__str__(self)} / Цена: {self.price}руб. / ' \
                f'Кол-во: {self.number}шт. / Разрешение: {str(self.resolution)}dpi'

    # метод ввода товара с обработкой ошибок
    def input_item(self):

        while True:
            try:
                title = input('Введите наименование оборудования: ')
                name = input('Введите наименование бренда: ')
                price = int(input('Введите цену за ед: '))
                number = int(input('Введите количество: '))
                item = {'Оборудование': title, 'Бренд': name, 'Цена': price, 'Кол-во': number}
                self.input_lists.update(item)
                self.my_sklad_temp.append(self.input_lists)
                print(f'Текущий список -\n {self.my_sklad_temp}')
            except ValueError:
                f'Ошибка ввода данных'
                return True

            print(f'Для выхода - Q, продолжение - Enter')
            q = input('>>>')
            if q == 'Q' or q == 'q':
                self.my_sklad.append(self.my_sklad_temp)
                print(f'Товары на складе -\n {self.my_sklad}')
                exit()
            else:
                Scaner.input_item(self)

sklad_1 = Sklad('Основной склад')
sklad_2 = Sklad('Пункт выдачи')

s = Scaner('Сканер', 'Epson', 10000, 10, 1440)
print(s)
x = Xerox('Ксерокс', 'Xerox', 7500, 15, 'ч/б')
print(x)
p = Printer('Принтер', 'HP', 20000, 3, 'A3')
print(p)

sklad_1.take_to_sklad(s)
sklad_1.take_to_sklad(x)
sklad_1.take_to_sklad(p)

sklad_2.moving_to_point(s)
sklad_1.moving_to_point(p)

print(s.input_item())

# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_number:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

cn_1 = Complex_number(1, -2)
cn_2 = Complex_number(3, 4)

print(cn_1 + cn_2)
print(cn_1 * cn_2)