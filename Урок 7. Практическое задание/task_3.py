"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
import random, timeit
from statistics import median

# Вариант 1

m = int(input('Введите параметр "m": '))
list_m = []
for i in range(2 * m + 1):
    list_m.append(random.randint(0, 10))

def func_1():
    i = 0
    ind = 0
    while i != len(list_m)-1:
        if list_m[i] <= list_m[i+1]:
            i, ind = ind, ind + 1
        else:
            list_m[i], list_m[i+1] = list_m[i+1], list_m[i]
            i -= 1
            if i < 0:
                i, ind = ind, ind + 1
    return list_m[m]

# Вариант 2

m = int(input('Введите параметр "m": '))
list_m = []
for i in range(2 * m + 1):
    list_m.append(random.randint(0, 10))

def func_2():
    i = len(list_m) // 2
    while i != 0:
        ind = list_m.index(max(list_m))
        list_m.pop(ind)
        i -= 1
    return max(list_m)

# Варинат 3

m = int(input('Введите параметр "m": '))
list_m = []
for i in range(2 * m + 1):
    list_m.append(random.randint(0, 10))

def func_3():
    med = median(list_m)
    return med

print(timeit.timeit(stmt="func_1()", setup="from __main__ import func_1",  number=10000))
print(timeit.timeit(stmt="func_2()", globals=globals(),  number=10000))
print(timeit.timeit(stmt="func_3()", setup="from __main__ import func_3",  number=10000))