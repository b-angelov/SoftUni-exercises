parentheses = {"[":"]","{":"}","(":")"}
stack = []
strng = input()
fail = False
for c in strng:
    is_opening = parentheses.get(c, None)
    if is_opening:
        stack.append(is_opening)
    elif stack and c == stack[-1]:
            stack.pop()
    else:
        fail = True
        break
else:
    if stack:
        print("NO")
    else:
        print("YES")
if fail:
    print("NO")
