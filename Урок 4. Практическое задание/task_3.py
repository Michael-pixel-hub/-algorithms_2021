"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

import timeit, cProfile

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    a = [enter_num[el-1] for el in range(len(enter_num))]
    return ''.join(a)

print(revers_4('1010'))

print(timeit.timeit(stmt="revers_1(2,20)", setup="from __main__ import revers_1",  number=10000))
print(timeit.timeit(stmt="revers_2(2,20)", setup="from __main__ import revers_2",  number=10000))
print(timeit.timeit(stmt="revers_3(20)", setup="from __main__ import revers_3",  number=10000))
print(timeit.timeit(stmt="revers_4('20')", setup="from __main__ import revers_4",  number=10000), '\n')

cProfile.run('revers_1(2,20)')
cProfile.run("revers_2(2,20)")
cProfile.run("revers_3(20)")
cProfile.run("revers_4('20')")

"""
Эффективнее revers_2 и revers_3, так как используют по 4 функции, остальные 5 и больше
"""