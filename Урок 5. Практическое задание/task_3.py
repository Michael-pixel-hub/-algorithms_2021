"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

# Задача 1

from collections import deque
from timeit import timeit

simple_list = []
deq_obj = deque()

def func_1():
    for i in 'bcddddddd':
        simple_list.append(i)

def func_2():
    for i in 'bcddddddd':
        deq_obj.append(i)

print(timeit(stmt="func_1()", setup="from __main__ import func_1",  number=10000))
# 0.0101819
print(timeit(stmt="func_2()", setup="from __main__ import func_2",  number=10000))
# 0.008375500000000001

"""
Заполнение очереди происходит быстрее, так как операции добавления имеют сложность O(1)
"""

# Задача 2

def func_3():
    simple_list.insert(0, "1")

def func_4():
    deq_obj.appendleft("1")

def func_5():
    a = simple_list.pop()
    return a

def func_6():
    a = deq_obj.popleft()
    return a

def func_7():
    simple_list.extend(['2', '3'])

def func_8():
    deq_obj.extendleft('23')

print(timeit(stmt="func_3()", setup="from __main__ import func_3",  number=10000))
# 0.9187539
print(timeit(stmt="func_4()", setup="from __main__ import func_4",  number=10000))
# 0.0015555999999999903
print(timeit(stmt="func_5()", setup="from __main__ import func_5",  number=10000))
# 0.0015081000000000122
print(timeit(stmt="func_6()", setup="from __main__ import func_6",  number=10000))
# 0.0014278999999999265
print(timeit(stmt="func_7()", setup="from __main__ import func_7",  number=10000))
# 0.002538200000000046
print(timeit(stmt="func_8()", setup="from __main__ import func_8",  number=10000))
# 0.002163000000000026


"""
Операции вставки и удаления сначала и конца у очередей происходят быстрее, так как сложность О(1). Однако все что
касается случайного доступа элемента, поиска по списку определенного элемента скорость списка будет быстрее. Это мы
видим в примерах выше
"""