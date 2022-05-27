name = ""

while name.lower() != "welcome!":
    name = str(input())
    if name.lower() == "welcome!":
        continue
    elif name.lower() == "voldemort":
        print("You must not speak of that name!")
        break
    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
else:
    print("Welcome to Hogwarts.")
