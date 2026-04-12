import random

while True: 

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\nWelcome to the Number Guessing Game!")
    print("You will have 5 attempts to guess a number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break

    if attempts == max_attempts and guess != number:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
    else:
        print(f"You guessed the number in {attempts} attempts!")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break