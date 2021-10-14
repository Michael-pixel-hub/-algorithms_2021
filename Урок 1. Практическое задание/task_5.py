"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

class StackClass:
    def __init__(self):
        self.elements = [[1,2,3,4,5,6]]
    def is_empty(self):
        return self.elements == []
    def push_in(self, el):
        if len(self.elements[len(self.elements)-1])-1 > 8:
            self.elements.append([el])
        else:
            self.elements[len(self.elements)-1].append(el)
    def pop_out(self):
        if len(self.elements[len(self.elements)-1])-1 < 1:
            return self.elements.pop()
        return self.elements[len(self.elements)-1].pop()
    def get_val(self):
        return self.elements[len(self.elements) - 1]
    def stack_size(self):
        sum_stack = 0
        for i in self.elements:
            sum_stack += len(i)
        return sum_stack
    def stack_count(self):
        return len(self.elements)
b = StackClass()
b.push_in(7)
b.push_in(8)
b.push_in(9)
b.push_in(10)
b.push_in(11)
b.push_in(12)
print(b.stack_size())
print(b.get_val())
print(b.elements)
print(b.stack_count())
b.pop_out()
print(b.elements)