"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

# Задание a

import time

def decorator (func):
    def wrapper (*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print(finish - start)
    return wrapper

@decorator
def dictionary_filling(len_dictionary): # сложность функции O(n)
    dictionary_one = {}
    for i in range(1, len_dictionary+1):
        dictionary_one[i] = ''
    return dictionary_one

@decorator
def list_filling(len_list): # сложность функции O(n)
    list_one = []
    for i in range(1,len_list+1):
        list_one.append(i)
    return list_one

dictionary_filling(10)
list_filling(10)

"""
Заполнение списка быстрее, чем словаря. Связано это с тем, что словарь создан на основе хеш-таблиц, 
т.е. "под капотом" производятся дополнительные операции (хеширование ключей) 
"""

# Задание b

dictionary_one = {1: 'a', 2: '3', 3: 'd', 4: 'q', 5: 'p'}
list_one = [1, 2, 3, 4, 5]

# вставка

@decorator
def paste_dictionary(name_dictionary, key, meaning): # сложность O(1)
    name_dictionary[key] = meaning

@decorator
def paste_list(name_list, meaning): # сложност O(1)
    name_list.append(meaning)

paste_dictionary(dictionary_one, 6, 'a')
paste_list(list_one, 6)

# удаление

@decorator
def delete_dictionary(name_dictionary, position): # сложность O(1)
    name_dictionary.pop(position)

@decorator
def delete_list(name_list, position): # сложность O(n)
    name_list.remove(position)

delete_dictionary(dictionary_one, 2)
delete_list(list_one, 2)

# получение

@decorator
def receiving_dictionary(name_dictionary, position): # сложность O(1)
    print(name_dictionary[position])

@decorator
def receiving_list(name_list, position): # сложность O(1)
    print(name_list[position])

receiving_dictionary(dictionary_one, 4)
receiving_list(list_one, 4)

"""
Словарь достает, вставляет и удаляет значения быстрее, так как работает на основе хеш-таблиц (выполняют операции по ключу). 
Список выполняет операции по индексу, поэтому он медленнее
"""