# There is no Block Scope in Python
# if-statements, while-loops, for-loops etc. don't get local scope

game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = "" # initialisation
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

