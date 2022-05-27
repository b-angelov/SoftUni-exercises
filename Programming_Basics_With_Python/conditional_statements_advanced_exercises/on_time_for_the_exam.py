exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

if exam_hour not in range(24) or arrival_hour not in range(24) or exam_minute not in range(60) or arrival_minute not in range(60):
    quit()

if exam_hour == 0:
    exam_hour = 24
if arrival_hour == 0:
    arrival_hour = 24

exam_minute_stamp = (exam_hour * 60) + exam_minute
arrival_minute_stamp = (arrival_hour * 60) + arrival_minute
difference = exam_minute_stamp - arrival_minute_stamp
message = ""

diff_difference = abs(difference) / 60
difference_time = ""

if difference != 0:
    if diff_difference >= 1:
        diff_modulus = abs(difference) % 60
        diff_min = str(diff_modulus)
        if diff_modulus < 10:
            diff_min = "0" + diff_min

        difference_time = f"{abs(difference) // 60}:{diff_min} hours"
    else:
        difference_time = f"{abs(difference)} minutes"

if 0 <= difference <= 30:
    print("On time")
    message = " before the start"
elif difference > 30:
    print("Early")
    message = " before the start"
elif difference < 0:
    print("Late")
    message = " after the start"


if difference_time != "":
    print(difference_time + message)