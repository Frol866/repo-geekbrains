# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary(time_of_work, bid, bonus):
    salary_employee = (float(time_of_work) * float(bid)) + float(bonus)
    print(f'Ваша зарплата: ', salary_employee)

script_name, time_of_work, bid, bonus = argv
salary(time_of_work, bid, bonus)


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

list_numbers = [randint(1, 1000) for _ in range(10)]
print(list_numbers)

i = 0
new_list_numbers = []

for el in list_numbers:
    if el > list_numbers[i-1]:
        new_list_numbers.append(el)
    i+=1

print(new_list_numbers)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

list_numbers = list(range(20, 240))
print(list_numbers)

new_list = [el for el in list_numbers if el % 20 == 0 or el % 21 == 0]
print(new_list)


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# Генерируем список чисел
list_numbers = [i * j for i in range(1, 3) for j in range(1, 5)]

#list_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список чисел: ', list_numbers)

# Поиск дубликатов чисел в исходном списке
repeat_numbers = [item for item in set(list_numbers) if list_numbers.count(item) > 1]

new_list = []

# Перебор элементов исходного списка и сравнение с дубликатами, в новый список записываем только те, которых нет в дубликате
for el in list_numbers:
    if el in repeat_numbers:
        continue
    else:
        new_list.append(el)

print('Новый список: ', new_list)



# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def multiplication(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

list_numbers = [i for i in range(100, 1001) if i % 2 == 0]
print(list_numbers)

print(reduce(multiplication, list_numbers))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#     Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

Решение А - скрипт для терминала
первый параметр - начальный элемент списка
второй параметр - конечный элемент списка

from sys import argv
from itertools import count

def list_numbers_a(start, stop):
    for el in count(int(start)):
        if el > int(stop):
            break
        else:
            result.append(el)
    return result

result = []
script_name, start, stop = argv
print(list_numbers_a(start, stop))


# Решение Б - скрипт для терминала
# первый параметр - что повторяем
# второй параметр - сколько раз повторяем

from sys import argv
from itertools import repeat

def list_numbers_b(list_repeat, number):
    result = [i for i in repeat(list_repeat, int(number))]
    return result

result = []
script_name, list_repeat, number = argv
print(list_numbers_b(list_repeat, number))

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial

def fact(n):
    for el in count(1):
        yield factorial(el)

n = int(input('Введите число для вычисления факториала: '))

gen = fact(n)
x = 0
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break
