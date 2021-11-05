"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
import timeit

a = []
for i in range(10):
    a.append(random.randint(-100, 100))

# вариант 1

def bubble():
    n = 1
    while n < len(a):
        for i in range(len(a)-n):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        n += 1

bubble()

# вариант 2

def bubble_2():
    n = 1
    while n < len(a):
        passage = True
        for i in range(len(a)-n):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                passage = False
        n += 1
        if passage:
            break

bubble_2()

print(timeit.timeit(stmt="bubble()", setup="from __main__ import bubble",  number=10000))
print(timeit.timeit(stmt="bubble_2()", setup="from __main__ import bubble_2",  number=10000))

"""
Доработал алгоритм "пузырька" тем, что добавил остановку, если список уже отсортирован. Алгоритм стал работать быстрее 
"""