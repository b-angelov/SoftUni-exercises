n1 = int(input())
n2 = int(input())
operator = str(input())
even = "even"

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    else:
        result = n1 * n2
    if result % 2 != 0:
        even = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even}")

elif operator == "/" or operator == "%":

    res_formatted = ""
    if n1 != 0 and n2 != 0:
        if operator == "/":
            result = n1 / n2
            res_formatted = f"{result:.2f}"
        elif operator == "%":
            result = n1 % n2
            res_formatted = str(result)
        print(f"{n1} {operator} {n2} = {res_formatted}")
    else:
        print(f"Cannot divide {n1} by zero")