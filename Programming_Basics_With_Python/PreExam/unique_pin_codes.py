first_number_upper_limit = int(input())  # 1/9
second_number_upper_limit = int(input())  # 1/9
third_number_upper_limit = int(input())  # 1/9

for a in range(2, first_number_upper_limit + 1, 2):
    for b in range(2, second_number_upper_limit + 1):
        if b > 7:
            continue
        not_prime = False
        for i in range(2, b + 1):
            if b % i == 0 and b != i:
                not_prime = True
                break
        if not_prime:
            continue
        for c in range(2, third_number_upper_limit + 1, 2):
                print(f"{a} {b} {c}")