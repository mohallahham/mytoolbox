import random


def get_user_input():
    while True:
        try:
            user_guess = int(
                input("What is your guess, it's a number between 1 and 100 ? ")
            )
            return user_guess

        except ValueError:
            print("Please enter a valid number")


def guessing_game():
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        print(f"you have {attempts} guesses left")

        user_guess = get_user_input()

        if user_guess == number:
            print(f" Yes, {number} was the correct number")
            break

        elif user_guess > number:
            print(f"{user_guess} is too high")

        else:
            print(f"{user_guess} is too low")

        attempts -= 1

    if attempts == 0:
        print(f"You've run out of attempts! The correct number was {number}.")


guessing_game()
