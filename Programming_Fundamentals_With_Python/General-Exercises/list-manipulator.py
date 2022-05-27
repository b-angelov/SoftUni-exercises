import sys

initial_list = input().split(" ") # list of integers
initial_list = list(map(int,initial_list))
command_string = "" # "exchange {index}" "max even" "max odd" "min even" "min odd" "first {n} even" "first {n} odd" "last {n} even" last n odd" "end"
min = sysmin = sys.maxsize
max = sysmax = -sys.maxsize

while command_string.lower() != "end":
    command = command_string = input()
    command = command.split(" ")
    len_command = len(command)
    if len_command == 2 and command[1].isdigit():
        # dealing with exchange
        if int(command[1]) > len(initial_list) or int(command[1]) < 0:
            print("Invalid index")
            continue
        initial_list = initial_list[int(command[1]) + 1:] + initial_list[:int(command[1]) + 1]
        # print(initial_list)
    elif len_command == 3 and command[1].isdigit():
        # dealing with first/last is even/odd
        if int(command[1]) > len(initial_list):
            print("Invalid count")
            continue

        pairs_even = []
        pairs_odd = []
        pair_even = []
        pair_odd = []
        for i in initial_list:

            if i % 2 == 0:
                pair_even.append(i)
                if len(pair_odd) > 1:
                    pairs_odd.append(pair_odd.copy())
                    pair_odd = []
            elif i % 2 != 0:
                pair_odd.append(i)
                if len(pair_even) > 0:
                    pairs_even.append(pair_even.copy())
                    pair_even = []

            if len(pair_even) > 0 :#and pair_even not in pairs_even:
                pairs_even.append(pair_even.copy())
            if len(pair_odd) > 0 :#and pair_odd not in pairs_odd:
                pairs_odd.append(pair_odd.copy())
            # if pair_even and len(pair_even) >= int(command[1]) and pair_even not in pairs_even:
            # if pair_even and pair_even not in pairs_even:
            #     pairs_even.append(pair_even)
            # # if pair_odd and len(pair_odd) >= int(command[1]) and pair_odd not in pairs_odd:
            # if pair_odd and pair_odd not in pairs_odd:
            #     pairs_odd.append(pair_odd)


        # if command[0] == "first":

        pair = []
        if command[2] == "even":
            for i in pairs_even:
                if len(i) == int(command[1]):
                    pair = i
                    break
            else:
                if len(pairs_even) > 0:
                    if command[0] == "first":
                        pair = pairs_even[0]
                    elif command[0] == "last":
                        pair = pairs_even[len(pairs_even) - 1]
        elif command[2] == "odd":
            for i in pairs_odd:
                if len(i) == int(command[1]):
                    pair = i
                    break
            else:
                if len(pairs_odd) > 0:
                    if command[0] == "first":
                        pair = pairs_odd[0]
                    elif command[0] == "last":
                        pair = pairs_odd[len(pairs_odd) - 1]
        print(pair)

        # elif command[0] == "last":
        #     if command[2] == "even":
        #         pass
        #     elif command[2] == "odd":
        #         pass
    else:
        if command[0] == "end":
            continue
        min_even = min_odd = min = sysmin
        max_even = max_odd = max = sysmax
        for i,v in enumerate(initial_list):
            if v < min:
                min = v
                if v % 2 == 0:
                    min_even = i
                else:
                    min_odd = i
            if v > max:
                max = v
                if v % 2 == 0:
                    max_even = i
                else:
                    max_odd = i
        if command[1] == "even":
            if command[0] == "max" and max_even != sysmax :
                print(max_even)
            elif command[0] == "min" and min_even != sysmin:
                print(min_even)
            else:
                print("No matches")


        elif command[1] == "odd":
            if command[0] == "max" and max_odd != sysmax:
                print(max_odd)
            elif command[0] == "min" and min_odd != sysmin:
                print(min_odd)
            else:
                print("No matches")


        # elif command[0] == "min":
        #     pass
        # elif command[0] == "max":
        #     pass
else:
    print(initial_list)
