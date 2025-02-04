import random
low = 1
high = 100
guesses = 0
num = random.randint(low, high)
while True:
    guess = int(input(f"Enter a number between ({low}-{high}): "))
    guesses += 1
    if guess < num:
        print(f"{guess} is too low")
    elif guess > num:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is corect")
        break
print(f"This round took you {guesses} guesses")
