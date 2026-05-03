enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Scope
player_health = 10 # It's available anywhere within the file


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion() # output: 2
# print(potion_strength) NameError
# potion_strength is defined in the function. We can only use it when we're inside that function