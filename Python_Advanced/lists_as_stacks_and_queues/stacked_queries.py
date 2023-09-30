stack = []
actions = {
    "1": lambda x: stack.append(int(x)),
    "2":lambda *x: stack.pop() if stack else None,
    "3": lambda *x: print(max(stack)) if stack else None,
    "4":lambda *x: print(min(stack)) if stack else None
}
n = int(input())
for _ in range(n):
    command = input().split()
    actions[command[0]](*command[1:])
print(", ".join(str(stack.pop()) for _ in range(len(stack))))