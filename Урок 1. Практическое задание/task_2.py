"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

# сложность #O(1) - линейная

def min_value(list_of_numbers):
    ind_max_number = len(list_of_numbers)-1 #O(1)
    ind_min_number = 0 #O(1)
    while ind_max_number != 0: #O(n)
        if list_of_numbers[ind_min_number] <= list_of_numbers[ind_max_number]: #O(1)
            ind_max_number = ind_max_number - 1 #O(1)
        elif list_of_numbers[ind_min_number] > list_of_numbers[ind_max_number]: #O(1)
            ind_min_number = ind_max_number #O(1)
            ind_max_number = ind_max_number - 1 #O(1)
    return list_of_numbers[ind_min_number] #O(1)

print(min_value([444,222,3333, 1, 3, 4, 4]))

# сложность O(n) - линейная

def min_value2(list_of_numbers):
    _min = list_of_numbers[0] #O(1)
    for i in list_of_numbers: #O(n)
        if i < _min: #O(1)
            _min = i #O(1)
    return _min #0(1)

print(min_value2([444,222,3333, 1, 3, 4, 4]))

# сложность O(n^2) - квадратичная

def min_value2(list_of_numbers):
    _min = list_of_numbers[0] #O(1)
    for i in list_of_numbers: #O(n)
        for j in list_of_numbers:  # O(n)
            if _min > j: #O(1)
                _min = j #O(1)
    return _min #0(1)

print(min_value2([444,222,3333, 1, 3, 4, 4]))