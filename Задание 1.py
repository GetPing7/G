''' Задание 1: Реализация стека с помощью массива '''

class Stack:
    def init(self, size=10):
        self.size = size
        self.stack = [None] * size
        self.top_index = -1

    def push(self, value):
        if self.is_full():
            print("Ошибка: Стек заполнен.")
        else:
            self.top_index += 1
            self.stack[self.top_index] = value
            print(f"Добавлено значение {value}.")

    def pop(self):
        if self.is_empty():
            print("Ошибка: Стек пуст.")
            return None
        else:
            popped_value = self.stack[self.top_index]
            self.stack[self.top_index] = None
            self.top_index -= 1
            return popped_value

    def top(self):
        if self.is_empty():
            print("Ошибка: Стек пуст.")
            return None
        else:
            return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.size - 1