hour = int(input())
minute = int(input())
next = minute + 15

if next != 60:
    remainder = 60 % next
else:
    remainder = next

if remainder == 60 :
    hour = hour + 1
    minute = next - 60
else:
    minute = next

if hour >= 24:
    hourPrint = "0"
else:
    hourPrint = str(hour)

if minute >= 60:
    minutePrint = "00"
else:
    minutePrint = str(minute)
    if minute < 10:
        minutePrint = "0" + minutePrint
print(f"{hourPrint}:{minutePrint}")
