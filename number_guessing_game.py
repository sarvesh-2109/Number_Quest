import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, attempts):
    """Checks whether the user guess against the answer. Returns the number of attempts remaining"""
    if guess > answer:
        print("Too High.")
        return attempts - 1
    elif guess < answer:
        print("Too Low")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    """Sets the difficulty level based on user input. Returns the number of attempts on basis of the level chosen."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a answer between 1 and 100.")
    answer = random.randint(1, 100)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the answer")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()




