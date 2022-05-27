number_sequence = input().split(" ")
number_sequence = list(map(int,number_sequence))
first_car = number_sequence[0 : len(number_sequence) // 2]
second_car = number_sequence[len(number_sequence) // 2 + 1:]
second_car.reverse()
time_first = time_second = 0
'''time_first = sum(first_car)
time_second = sum(second_car)
if first_car.count(0) > 0:
    time_first *= 0.8
if second_car.count(0) > 0:
    time_second *= 0.8'''
for i in range(len(first_car)):
    time_first += first_car[i]
    if first_car[i] == 0:
        time_first *= 0.8
for i in range(len(second_car)):
    time_second += second_car[i]
    if second_car[i] == 0:
        time_second *= 0.8

winner = ["right",time_second]
if time_first < time_second:
    winner = ["left", time_first]

print(f"The winner is { winner[0]} with total time: {winner[1]:.1f}")
