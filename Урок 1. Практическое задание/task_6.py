"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
class StackClass2:
    def __init__(self):
        self.tasks = [1,2,3,4,5,6]
        self.solved = []
        self.unresolved = []
    def is_empty(self):
        return self.elements, self.solved, self.unresolved == []
    def push_in(self, task):
        self.tasks.insert(0, task)
    def push_in_solved(self):
        self.solved.insert(0, self.tasks.pop())
    def push_in_unresolved(self):
        self.unresolved.insert(0, self.tasks.pop())

c = StackClass2()
c.push_in(7)
c.push_in_solved()
c.push_in_unresolved()
print(c.tasks)
print(c.solved)
print(c.unresolved)