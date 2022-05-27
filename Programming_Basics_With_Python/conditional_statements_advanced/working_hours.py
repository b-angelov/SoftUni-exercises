day_hour = int(input())
day = str(input())

if 10 <= day_hour <= 18 and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print("open")
else:
    print("closed")
