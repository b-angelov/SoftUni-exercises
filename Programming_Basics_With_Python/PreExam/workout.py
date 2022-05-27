import math

N_count_days = int(input())  # 1/50
M_count_kilometers_first_day = float(input())  # 1.00/500.00
K_daily_norm_increase_percent = 0
days_ran = M_count_kilometers_first_day
ran = 0


for i in range(N_count_days + 1):
    increase = days_ran * (K_daily_norm_increase_percent / 100)
    days_ran = days_ran + increase
    ran += days_ran
    if i == N_count_days:
        continue

    K_daily_norm_increase_percent = int(input())  # 1/100


if ran >= 1000:
    print(f"You've done a great job running {math.ceil(ran - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - ran)} more kilometers")

