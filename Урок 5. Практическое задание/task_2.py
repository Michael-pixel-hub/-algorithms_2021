"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict
from functools import reduce

# a = 'A2'
# b = 'C4F'
# c = ['C4F', 'A2']
# e = int(a, 16) + int(b, 16)
# print(e)

list_calculator = defaultdict(list)

number_1 = input('Введите первое число: ')
for i in number_1:
    list_calculator[1].append(i)

number_2 = input('Введите второе число: ')
for i in number_2:
    list_calculator[2].append(i)

list_calculator_join = ''.join(list_calculator[1]), ''.join(list_calculator[2])
sum_all = format(reduce(lambda x,y: int(x, 16) + int(y, 16), list_calculator_join), 'X')
for i in sum_all:
    list_calculator['sum_all'].append(i)
composition_all = format(reduce(lambda x,y: int(x, 16) * int(y, 16), list_calculator_join), 'X')
for i in composition_all:
    list_calculator['composition_all'].append(i)

print(list_calculator)