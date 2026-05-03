import random

import art

print("\n")
print(art.logo)
print("\n")
print("Welcome to the Number Guessing Game!\n"
      "I'm thingking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt = 0 # init
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5
else:
    print("Invalid. You have to type 'easy' or 'hard'.")

answer = random.choice(range(1,101))

while attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("Your guess is correct!\n"
              f"It was {answer}.")
        break
    attempt -= 1
    if attempt == 0:
        print("You've run out of guesses, you lose.\n"
              f"It was {answer}.")
    else:
        print("Guess again.")