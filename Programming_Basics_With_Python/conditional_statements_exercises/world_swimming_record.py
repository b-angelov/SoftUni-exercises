worldRecord = float(input())
distance = float(input())
timePerMeter = float(input())
waterResistance = 12.5
time = timePerMeter * distance

delay = (distance // 15) * waterResistance
finishTime = time + delay

if finishTime < worldRecord:
    print(f"Yes, he succeeded! The new world record is {finishTime:.2f} seconds.")
else:
    print(f"No, he failed! He was {(finishTime - worldRecord):.2f} seconds slower.")
