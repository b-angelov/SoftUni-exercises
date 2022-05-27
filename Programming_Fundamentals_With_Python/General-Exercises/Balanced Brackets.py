lines = int(input())
brake_bracket = ")"
pass_bracket = "("

for i in range(lines):
    string = input()
    if string == brake_bracket:
        print("UNBALANCED")
        break
    elif string == pass_bracket:
        brake_bracket, pass_bracket = pass_bracket, brake_bracket
else:
    print("BALANCED")