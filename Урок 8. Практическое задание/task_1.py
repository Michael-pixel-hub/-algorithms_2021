"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

import collections

str_one = 'Вася'  # создали строку
obj = collections.Counter(str_one).items()  # создали тип данных каунтер, вернули список картежей: ключ и значение
obj_sort = sorted(obj, key=lambda x: x[1])  # отсортировали список по значениям
list_one = tuple
while len(obj_sort) >= 2:
    cut = obj_sort[0:2]  # берем первые 2 элемента списка
    del obj_sort[0:2]  # удаляем первые 2 эелемнта списка
    sum_ = cut[0][1] + cut[1][1]  # скалдываем значения первых 2 элементов
    list_one = ({1: cut[0][0], 0: cut[1][0]},
                sum_)  # создаем словарь с ключами 0 и 1, первый элемент вставляем в ключ 0, а второй в 1
    for i in obj_sort[:]:
        a = 0
        if i == obj_sort[-1]:
            obj_sort.append(list_one)
        elif sum_ <= i[1]:
            ind = obj_sort.index(i)
            obj_sort.insert(ind, list_one)
            break
        elif sum_ > i[1]:
            continue
        a += 1 # создаем структуру алгоритма Хаффмана

list_two = list_one[0]
code_table = dict()


def code(dict_, path=''):
    if not isinstance(dict_, dict):
        code_table[dict_] = path
    else:
        code(dict_[0], path=f'{path}0')
        code(dict_[1], path=f'{path}1')


code(list_two) # создаем таблицу кодировки

print(str_one)

for i in str_one:
    print(code_table[i], end='')