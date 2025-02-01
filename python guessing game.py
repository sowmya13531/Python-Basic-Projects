import random

low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True

print("Python Number guessing game")
print(f"Select a num b/w {low_num} and {high_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low_num or guess > high_num:
            print("The number is out the set of numbers")
            print(f"Please select a number between {low_num} and {high_num}: ")
        elif guess < answer:
            print("Too low: Try again")
        elif guess > answer:
            print("Too high: Try again")
        else:
            print(f"CORRECT The answer {answer} ")
            print(f"No.of guesses: {guesses}")


    else:
        print("Invalid guess")
        print(f"Please select a number between {low_num} and {high_num}: ")

