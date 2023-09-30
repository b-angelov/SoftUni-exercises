from collections import deque

sequence_a,sequence_b = [set(map(int,input().split())) for _ in range(2)]
funcs = {
    "Add First ": lambda seq: sequence_a.update(set(seq)),
    "Add Second ": lambda seq: sequence_b.update(set(seq)),
    "Remove First ": lambda seq: sequence_a.difference_update(set(seq)),
    "Remove Second ": lambda seq: sequence_b.difference_update(set(seq)),
    "Check Subset": lambda seq: print(set(sequence_a).issubset(sequence_b) or set(sequence_b).issubset(sequence_a))
}

for _ in range(int(input())):
    command = input()
    operation = [key for key in funcs.keys() if command.startswith(key)]
    fn = operation[0] if operation else command
    res = funcs[fn](list(map(int,command.split(operation[0])[1].split())))
print(", ".join(str(i) for i in sorted(sequence_a)),", ".join(str(i) for i in sorted(sequence_b)),sep="\n")