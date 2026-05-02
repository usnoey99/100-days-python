# Blackjack Project - Rules
import random

# 1. The deck is unlimited in size
# 2. There are no jockers
# 3. The Jack/Queen/ King all count as 10
# 4. The Ace can count as 11 or 1

from art import logo


# function to calculate total the cards values
def calculate(cardslist):
    total = sum(cardslist)
    while total > 21 and 11 in cardslist:
        # Ace card as 1
        ace_index = cardslist.index(11)
        cardslist[ace_index] = 1
        total = sum(cardslist)
    return total

# fuction to ask to play a game
def ask():
    play = input("Do you want to play a game of Blackjack? Type 'y' for 'n': ").lower()
    if play == "y":
        return True
    elif play == "n":
        return False
    else:
        print("Invalid. Type again please.")
        return ask()

# function to compare the scores
def compare(playertotal, computertotal):
    print(f"Your final hand: {player}, final score: {player_total}")
    print(f"Computer's final hand: {computer}, final score: {computer_total}")
    if playertotal > 21:
        print("You went over. You lose 😭")
    elif computertotal > 21:
        print("Computer went over. You win 😁")
    elif playertotal > computertotal:
        print("You are the winner 😁")
    elif playertotal < computertotal:
        print("You lost with a lower score 😭")
    else:
        print("Draw 🙃")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("\n")
print(logo)
print("\n")
isStart = ask()

while isStart :
    print("\n"*20)
    print(logo)
    print("\n")

    player = []
    computer = []  # also dealer
    isContinue = True
    # two starting cards in the hand
    for _ in range(2):
        player.append(random.choice(cards)) # player = [first_pcard, second_pcard]
        computer.append(random.choice(cards)) # computer = [first_dcard, second_dcard]



    while isContinue:
        player_total = calculate(player)
        computer_total = calculate(computer)
        print(f"Your cards: {player}, current score: {player_total}")
        print(f"Computer's first card: {computer[0]}")

        if player_total > 21:
            compare(player_total,computer_total)
            break

        if computer_total == 21 and len(computer) == 2:
            # computer wins
            print(f"Computer's final hand: {computer}, final score: {computer_total}")
            print("Blackjack for the computer. Better luck next time. 🂡")
            break
        elif player_total == 21 and len(player) == 2:
            # player wins
            print(f"Your final hand: {player}, final score: {player_total}")
            print("You got a Blackjack! You win 👑")
            break

        # ask to get another card
        nextround = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if nextround == "y":
            next_pcard = random.choice(cards)
            player.append(next_pcard)

        elif nextround == "n":
            # final score
            while computer_total < 17:
                next_ccard = random.choice(cards)
                computer.append(next_ccard)
                computer_total = calculate(computer)
            compare(player_total, computer_total)
            isContinue = False

    isStart = ask()