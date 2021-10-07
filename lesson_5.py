# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file.txt', 'w')

while True:
    stroka = input("Введите данные: ")

    if not stroka:
        print('Ввод завершен')
        exit()
    else:
        f_obj.write(stroka + '\n')

f_obj.close()

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_2.txt', 'r', encoding='utf-8')

i = 0
for line in f_obj:
    i +=1
    list_line = line.split(' ')
    print(f'Кол-во слов в {i} строке равно: ', len(list_line))

print('Кол-во строк в файле: ', i)
f_obj.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_3.txt', 'r', encoding='utf-8')

zp = []
family = []
average = []

# считываем строки из файла и создаем список
my_list = f_obj.read().split('\n')
print(my_list)

for i in my_list:
    i = i.split() # Делаем списки в цикле с Фамилией и ЗП
    average.append(i[1])
    if int(i[1]) < 20000: # И если ЗП меньше 20 000р
        family.append(i[0]) # Фамилию пишем в отдельный список
        zp.append(i[1]) # ЗП в другой список

# Находим среднюю ЗП
result = 0
for el in average:
    result = result + int(el)
average_zp = result/len(average)

print(f'Сотрудники {family} получают оклад меньше 20000 руб. Средний оклад {average_zp} руб.')
f_obj.close()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_numbers = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_4.txt', 'r', encoding='utf-8')

data_for_new_file = []
for i in f_obj:
    i = i.split(' ', 1)
    data_for_new_file.append(dict_numbers[i[0]] + ' ' + i[1])

print(data_for_new_file)

f_obj_2 = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_4_result.txt', 'w', encoding='utf-8')
f_obj_2.writelines(data_for_new_file)

f_obj.close()
f_obj_2.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

def summma(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return int(prev_el) + int(el)

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_5.txt', 'w', encoding='utf-8')

numbers = ['1 2 3 4 5 6 7 8 9 10']
f_obj.writelines(numbers)

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_5.txt', 'r', encoding='utf-8')
for i in f_obj:
    list_numbers = i.split(' ')
    print(list_numbers)

print(f'Сумма чисел в файле равна: ', reduce(summma, list_numbers))

f_obj.close()

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

f_obj = open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_6.txt', 'r', encoding='utf-8')

predmet_dict = {}

for line_file in f_obj:
    subject, lecture, practice, lab = line_file.split()

    lek = lecture.split('(')
    prak = practice.split('(')
    l = lab.split('(')

    if lek[0] == '-':
        lek[0] = 0

    if prak[0] == '-':
        prak[0] = 0

    if l[0] == '-':
        l[0] = 0


    all = int(lek[0]) + int(prak[0]) + int(l[0])

    new_dict = {}
    dict_fin = {(subject, all)}
    new_dict.update(dict_fin)
    print(new_dict)

f_obj.close()


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_7.txt', 'r', encoding='utf-8') as f_obj:
    list_profit = []
    list_dict = {}
    temp_list = []
    temp_dict = {}

    for line in f_obj:

        name, forma, proceeds, costs = line.split()
        profit = int(proceeds) - int(costs)
        print(f'Прибыль фирмы {name} равна {profit}')

        # Создаем словарь из элементов списка
        list_dict[name] = profit

        if profit > 0:
            list_profit.append(profit)
        else:
            continue


average_profit = sum(list_profit)/len(list_profit)
print(f'Средняя прибыль равна: {average_profit}')

# Создаем словарь средней прибыли
temp_dict['average_profit'] = average_profit
# Создаем список из наших двух словарей
temp_list.append(list_dict)
temp_list.append(temp_dict)

with open(r'C:\Users\Dell XPS\Desktop\ИИ и Нейросети\Основы языка Python\my_file_7.json', 'w', encoding='utf-8') as json_obj:
    json.dump(temp_list, json_obj)
