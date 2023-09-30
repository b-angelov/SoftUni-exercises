from collections import deque

bullet_price, barrel_size, bullets, locks, payment = tuple(input() for _ in range(5))
bullets_price, barrel_size, payment = int(bullet_price),int(barrel_size),int(payment)
bullets = list(map(int,bullets.split()))
locks = deque(map(int,locks.split()))
barrel = barrel_size

while bullets and locks:
    bullet = bullets.pop()
    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    payment -= bullets_price
    barrel -= 1

    if bullets and not barrel:
        print("Reloading!")
        barrel = barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${payment}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")