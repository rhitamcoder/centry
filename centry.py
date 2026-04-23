import random

logo = r"""
    ___           _              
  / __\___ _ __ | |_ _ __ _   _ 
 / /  / _ \ '_ \| __| '__| | | |
/ /__|  __/ | | | |_| |  | |_| |
\____/\___|_| |_|\__|_|   \__, |
                          |___/ 
"""

print(logo)

print("Welcome to the Number Guessing Game!")

print("I am thinking of a number between 1 and 100.")

secret_num = random.randint(1, 100)

def play_game(attempts_allowed):
    for attempts in range(1, attempts_allowed + 1):
        remaining = attempts_allowed - attempts + 1
        print(f"You have {remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > secret_num:
            print("Too High")
        elif guess < secret_num:
            print("Too Low")
        elif guess == secret_num:
            print(f"You got it! The answer was {secret_num}.")
            return

        if remaining > 1:
            print("Guess again.")
        else:
            print("You've run out of guesses, you loss.")

difficulty = ""
while difficulty not in ["easy", "hard"]:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty not in ["easy", "hard"]:
        print("👀ps! Please type 'easy' or 'hard'.")


if difficulty == "easy":
    play_game(10)
elif difficulty == "hard":
    play_game(5)





