import math

movie = str(input())
episode_length = int(input())
break_duration = int(input())
lunch_time = break_duration / 8
rest_time = break_duration / 4
time = (break_duration - lunch_time - rest_time) - episode_length

if time >= 0:
    time = math.ceil(abs(time))
    print(f"You have enough time to watch {movie} and left with {int(time)} minutes free time.")
else:
    time = math.ceil(abs(time))
    print(f"You don't have enough time to watch {movie}, you need {int(time)} more minutes.")