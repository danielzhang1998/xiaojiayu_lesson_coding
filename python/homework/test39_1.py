class Stack:
    def __init__(self, start = []):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if self.isEmpty():
            print('Warning, the stack is empty!')
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            print('Warning, the stack is empty!')
        else:
            return self.stack[-1]

    def bottom(self):
        if self.isEmpty():
            print('Warning, the stack is empty!')
        else:
            return self.stack[0]

    def print_all(self):
        if self.isEmpty():
            print('Warning, the stack is empty!')
        else:
            return self.stack

stack1 = Stack([1,2,3,4,5])
print(stack1.isEmpty())
stack1.push(666)
print(stack1.pop())
print(stack1.top())
print(stack1.bottom())
print(stack1.print_all())