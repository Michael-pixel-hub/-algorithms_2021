"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage
import timeit

def optimization(func):
    def wrapper(*args, **kwargs):
        time_start = timeit.default_timer()
        m1_memory = memory_usage()
        func(*args, **kwargs)
        m2_memory = memory_usage()
        time_end = timeit.default_timer() - time_start
        memory = m2_memory[0] - m1_memory[0]
        return f'Память - {memory}\nВремя - {time_end}\n'
    return wrapper

# Скрипт 1

@optimization
def func1():
    list_namber = []
    for i in range(1, 1000, 2):
        list_namber.append(i**3) #сделал список нечетных чисел, возведенных в 3 степень (от 1 до 1000)
    sum_total = 0
    for i in list_namber:
        sum_namber = 0
        new_namber = i
        while new_namber > 0: #делю число на составляющие числа и складываю их
            a = new_namber % 10
            sum_namber = sum_namber + a
            new_namber = new_namber // 10
            if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
                sum_total = sum_total + i
    sum_total = 0 #обнуляю переменную
    for i in list_namber:
        sum_namber = 0
        new_namber = i + 17 #прибавляю к каждому элементу списка 17
        while new_namber > 0: #делю число на составляющие числа и складываю их
            a = new_namber % 10
            sum_namber = sum_namber + a
            new_namber = new_namber // 10
            if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
                sum_total = sum_total + i
print(func1())

@optimization
def func2():
    list_namber = (i**3 for i in range(1, 1000, 2)) #сделал список нечетных чисел, возведенных в 3 степень (от 1 до 1000)
    sum_total = 0
    for i in list_namber:
        sum_namber = 0
        new_namber = i
        while new_namber > 0: #делю число на составляющие числа и складываю их
            a = new_namber % 10
            sum_namber = sum_namber + a
            new_namber = new_namber // 10
            if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
                sum_total = sum_total + i
    sum_total = 0 #обнуляю переменную
    list_namber = (i ** 3 for i in range(1, 1000, 2))
    for i in list_namber:
        sum_namber = 0
        new_namber = i + 17 #прибавляю к каждому элементу списка 17
        while new_namber > 0: #делю число на составляющие числа и складываю их
            a = new_namber % 10
            sum_namber = sum_namber + a
            new_namber = new_namber // 10
            if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
                sum_total = sum_total + i

print(func2())

"""
Для профилирования памяти в func2 заменил массивы на генераторы. За счет этого дополнительной памяти не потребовалось
"""

# Скрипт 2

import numpy, random
from memory_profiler import profile

@optimization
def func3(quantity):
    list_finsh = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < quantity:
        list_joke = [random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]
        a = ' '.join(list_joke)
        list_joke.clear()
        list_finsh.append(a)
        i += 1

print(func3(5))

@optimization
def func4(quantity):
    list_finsh = []
    nouns = ("автомобиль", "лес", "огонь", "город", "дом")
    adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
    adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
    i = 0
    while i < quantity:
        list_joke = (random.choice(nouns), random.choice(adverbs), random.choice(adjectives))
        a = ' '.join(list_joke)
        list_finsh.append(a)
        i += 1

print(func4(5))

"""
Вместо массива использовал картеж. Картеж использует меньше памяти, поэтому доп. памяти не потребовалось
"""

# Скрипт 3

from recordclass import recordclass

class Road1:

    _length = 5
    _width = 10
    def __init__(self, mass, blade_thickness):
        mass_of_asf = Road1._length*Road1._width*mass*blade_thickness
        print(f'{Road1._length} м * {Road1._width} м * {mass} кг * {blade_thickness} см = {mass_of_asf}')

time_start = timeit.default_timer()
m1_memory = memory_usage()
Road1(3,4)
m2_memory = memory_usage()
time_end = timeit.default_timer() - time_start
memory = m2_memory[0] - m1_memory[0]
print(f'Память - {memory}\nВремя - {time_end}\n')

class Road2:
    _length = 5
    _width = 10
    __slots__ = ['mass', 'blade_thickness']
    def __init__(self, mass, blade_thickness):
        mass_of_asf = Road2._length*Road2._width*mass*blade_thickness
        print(f'{Road2._length} м * {Road2._width} м * {mass} кг * {blade_thickness} см = {mass_of_asf}')

time_start = timeit.default_timer()
m1_memory = memory_usage()
Road2(3,4)
m2_memory = memory_usage()
time_end = timeit.default_timer() - time_start
memory = m2_memory[0] - m1_memory[0]
print(f'Память - {memory}\nВремя - {time_end}\n')

"""
Оптимизировал класс с помощью слотов. За основу аргументов взял список. Дополнительной памяти не потребовалось
"""