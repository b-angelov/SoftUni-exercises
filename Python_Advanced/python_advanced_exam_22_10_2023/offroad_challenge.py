from collections import deque

initial_fuel = deque(map(int, input().split()))
additional_consumption_index = deque(map(int, input().split()))
necessary_fuel_amount = deque(map(int, input().split()))
altitude = 0

while initial_fuel and additional_consumption_index and necessary_fuel_amount:
    fuel = initial_fuel.pop()
    index = additional_consumption_index.popleft()
    res = fuel - index
    if res >= necessary_fuel_amount[0]:
        necessary_fuel_amount.popleft()
        print(f"John has reached: Altitude {altitude + 1}")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break
    altitude += 1

if necessary_fuel_amount:
    if altitude > 0:
        print(f"John failed to reach the top.\nReached altitudes: {', '.join(f'''Altitude {n}''' for n in range(1, altitude + 1))}"
              )
    else:
        print("John failed to reach the top.\nJohn didn't reach any altitude."
              )
else:
    print("John has reached all the altitudes and managed to reach the top!")
