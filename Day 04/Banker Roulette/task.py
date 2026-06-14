import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# ran_i = random.randint(0,4)
# bill_person = friends[ran_i]
# print(f">>{bill_person}<< should pay for lunch today!")

bill_person = random.choice(friends)
print(f">>{bill_person}<< should pay for lunch today!")
