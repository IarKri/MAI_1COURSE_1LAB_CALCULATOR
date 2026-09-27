class Stack:
    '''
    Стэк на основе списка

    Хранит в себе значения

    Attributes:
        items: список, для хранения элементов
    '''
    def __init__(self):
        '''
        создание пустого списка, в котором будут лежать элементы
        '''
        self.items = []

    def push(self, item):
        '''
        Добавление элемента в стэк

        Args:
            item: элемент, добавляемый в стэк
        '''
        self.items.append(item)

    def pop(self):
        '''
        Удаление верхнего элемента из стэка с выводом

        Returns: последний эдемент стэка
        '''
        return self.items.pop()

    def is_empty(self):
        '''
        проверка стэка на пустоту
        '''
        return not self.items

    def last(self):
        '''
        вывод последнего элемента стэка
        '''
        if self.items:
            return self.items[-1]

    def size(self):
        '''
        длина стэка
        '''
        return len(self.items)

