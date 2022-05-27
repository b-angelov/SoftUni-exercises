import sys

snowballs = int(input())
best_snowball = -sys.maxsize
features = {}

for ball in range(snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    ball_score = (weight / time_to_target) ** quality
    if ball_score > best_snowball:
        best_snowball = ball_score
        features = {"weight":weight, "time_to_target" : time_to_target, "value": ball_score,"quality":quality}


print(f"{features['weight']} : {features['time_to_target']} = {int(features['value'])} ({features['quality']})")
