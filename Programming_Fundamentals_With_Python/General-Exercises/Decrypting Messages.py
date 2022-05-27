key = int(input())
lines = int(input())
out = ""

for i in range(lines):

    character = input()
    out += chr(ord(character) + key)

print(out)
