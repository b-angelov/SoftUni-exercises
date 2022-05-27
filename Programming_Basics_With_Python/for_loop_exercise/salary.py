browser_tabs = int(input())
salary = int(input())
tax = 0

if 1 <= browser_tabs <= 10 and 500 <= salary <= 1500:
    for i in range(0, browser_tabs):
        site = str(input())
        if site == "Facebook":
            tax += 150
        elif site == "Instagram":
            tax += 100
        elif site == "Reddit":
            tax += 50

        if tax >= salary:
            salary = 0
            print("You have lost your salary.")
            break

    if salary != 0:
        print(f"{salary - tax}")