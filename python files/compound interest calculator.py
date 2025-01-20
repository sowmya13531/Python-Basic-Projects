#Python compound interest calculator

principle = 0
time = 0
rate = 0
while True:
    principle = float(input("Enter the priniple amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("Rate can't be less than zero")
    else:
        break
while True:
    time = float(input("Enter the Time in yrs: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} yr/s: ${total:.2f}")