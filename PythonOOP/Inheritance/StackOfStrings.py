from collections import deque


class Stack:
    def __init__(self):
        self.data = deque()

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return f'{self.data[-1]}'

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def __str__(self):
        return f'[{", ".join([str(x) for x in self.data.__reversed__()])}]'


s = Stack()
s.push('abc')
s.push('a21')
print(s)
s.push('a12')
print(s.top())
print(s.pop())
print(s)
