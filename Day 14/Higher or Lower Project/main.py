from multiprocessing.connection import answer_challenge

from art import logo, vs
from game_data import data
from random import choice

# def ask - input: Who has more followers? Type 'A' or 'B':
def ask():
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return  answer
# def compare
def compare(dictionaryA, dictionaryB):
    # Compare A: name, description, from country
    print(f"Compare A: {dictionaryA["name"]}, {dictionaryA["description"]}, from {dictionaryA["country"]}.")
    # art.vs
    print("\n")
    print(vs)
    # Against B: name, description, from country
    print(f"Against B: {dictionaryB["name"]}, {dictionaryB["description"]}, from {dictionaryB["country"]}.")

    if dictionaryA["follower_count"] > dictionaryB["follower_count"] :
        return "a"
    else:
        return "b"

game_data = data
is_game_over = False
score = 0
# initial
compareA = choice(game_data)
game_data.remove(compareA)

print("\n" * 20)
print(logo)

while not is_game_over:
    againstB = choice(game_data)
    game_data.remove(againstB)

    result = compare(compareA, againstB)
    # input user's answer
    answer = ask()

    # if the choice is correct
    if answer == result :
        # score ++
        score += 1
        print("\n" * 20)
        print(logo)
        # You're right! Current score
        print(f"You're right! Current score: {score}")
        # Compare A = Against B, next ask()
        compareA = againstB
    # else not correct
    else:
        # Sorry, that's wrong. Final score:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True

    if not game_data:
        print(f"You achieve the maximum score! You win! Final score: {score}")
        is_game_over = True
