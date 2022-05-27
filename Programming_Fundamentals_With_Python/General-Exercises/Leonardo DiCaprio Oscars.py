number = int(input())

match number:
    case 88:
        print("Leo finally won the Oscar! Leo is happy")
    case 86:
        print("Not even for Wolf of Wall Street?!")
    case number if number < 88:
        print("When will you give Leo an Oscar?")
    case _:
        print("Leo got one already!")