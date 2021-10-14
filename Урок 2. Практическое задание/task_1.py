"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

"""

Вариант с циклом

while True:
    try:
        list_action = ['+', '-', '*', '/']
        user_action = input('Введите операцию (+, -, *, / или 0 для выхода):')
        if user_action == '0':
            break
        elif user_action not in list_action:
            raise Exception ('Несоответсвтующее значение')
        user_number_one = int(input('Введите первое число:'))
        user_number_two = int(input('Введите второе число:'))
        if user_action == '+':
            answer = user_number_one + user_number_two
            print(answer)
        elif user_action == '-':
            answer = user_number_one - user_number_two
            print(answer)
        elif user_action == '*':
            answer = user_number_one * user_number_two
            print(answer)
        elif user_action == '/':
            answer = user_number_one / user_number_two
            print(answer)
    except ZeroDivisionError:
        print('На 0 делить нельзя') 
    except ValueError:
        print('Значение должно быть типа "int"')
    except Exception:
        print('Неправильно ввели операцию. Нужно ввести один из вариантов: +, -, *, /')
        continue
"""
# Вариант с рекурсией

def calculator():
    try:
        list_action = ['+', '-', '*', '/']
        user_action = input('Введите операцию (+, -, *, / или 0 для выхода):')
        # базовый случай
        if user_action == '0':
            pass
        elif user_action not in list_action:
            raise Exception ('Несоответсвтующее значение')
        else:
            user_number_one = int(input('Введите первое число:'))
            user_number_two = int(input('Введите второе число:'))
            if user_action == '+':
                answer = user_number_one + user_number_two
                print(answer)
            elif user_action == '-':
                answer = user_number_one - user_number_two
                print(answer)
            elif user_action == '*':
                answer = user_number_one * user_number_two
                print(answer)
            elif user_action == '/':
                answer = user_number_one / user_number_two
                print(answer)
            return calculator()
    except ZeroDivisionError:
        print('На 0 делить нельзя')
        return calculator()
    except ValueError:
        print('Значение должно быть типа "int"')
        return calculator()
    except Exception:
        print('Неправильно ввели операцию. Нужно ввести один из вариантов: +, -, *, /')
        return calculator()

calculator()