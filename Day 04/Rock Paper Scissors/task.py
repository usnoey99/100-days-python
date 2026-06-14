import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
print(play[user_choice])
compter_choice = random.randint(0,2)
print(play[compter_choice])

if user_choice != compter_choice:
    if user_choice == 0 and compter_choice == 1:
        print("You lose the game.")
    elif user_choice == 0 and compter_choice == 2:
        print("You win the game!")
    elif user_choice == 1 and compter_choice == 2:
        print("You lose the game.")
    elif user_choice == 1 and compter_choice == 0:
        print("You win the game!")
    elif user_choice == 2 and compter_choice == 0:
        print("You lose the game.")
    elif user_choice == 2 and compter_choice == 1:
        print("You win the game!")
elif user_choice == compter_choice:
    print("It's a draw.")
else:
    input("Invalid.")