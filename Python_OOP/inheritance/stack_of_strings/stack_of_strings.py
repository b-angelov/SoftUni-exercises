class Stack:

    def __init__(self):
        self.data = []

    def push(self,element: str):
        if type(element) != str:
            raise Exception("Non strings have beeen excluded")
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __repr__(self):
        return f"[{', '.join(self.data[::-1])}]"

stack = Stack()
stack.push("apple")
stack.push("carrot")
print(stack.top())
print(stack.pop())
print(stack.is_empty())
stack.push("pineapple juice")
print(stack)