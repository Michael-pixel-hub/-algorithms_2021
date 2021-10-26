"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
import collections

dict_one = {1: 'hello', 2: 'vvv', 3: 'ddd'}
dict_ordereddict = collections.OrderedDict([(1, 'hello'), (2, 'vvv'), (3, 'ddd')])

def func_1():
    for i in range(4,8):
        dict_one[i] = 'hello'

def func_2():
    for i in range(4,8):
        dict_ordereddict[i] = 'hello'

def func_3():
    return dict_one[1]

def func_4():
    return dict_ordereddict[1]

print(timeit(stmt="func_1()", setup="from __main__ import func_1",  number=10000))
# 0.005635399999999999
print(timeit(stmt="func_2()", setup="from __main__ import func_2",  number=10000))
# 0.011919599999999995
print(timeit(stmt="func_3()", setup="from __main__ import func_3",  number=10000))
# 0.0011161999999999977
print(timeit(stmt="func_4()", setup="from __main__ import func_4",  number=10000))
# 0.001102800000000001

"""
В случае заполнения словаря коллекция ordereddict была медленнее, чем словарь. В случае получения ключа незначительно
быстрее оказался ordereddict.
Смысла использовать ordereddict в Python 3.6 и выше не вижу, так как он медленнее, а в новых версиях словарь упорядочен
"""