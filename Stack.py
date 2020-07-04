class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, v):
        self.__stack.append(v)

    def pop(self):
        return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return self.__stack == []


s = Stack()
print(f"The stack is empty - {s.is_empty()}")
s.push("first")
s.push("second")
print(f"Stack size - {len(s)}")
print(f"The stack is empty - {s.is_empty()}")
print(s.pop())
print(s.pop())
print(f"The stack is empty - {s.is_empty()}")
