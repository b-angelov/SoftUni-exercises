username = str(input())
password = str(input())

while True:
    mess = str(input())

    if mess == password:
        break
print(f"Welcome {username}!")