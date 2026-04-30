import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

simple_password = ""
hard_password = []

for char in range(0,nr_letters): # range(1,nr_numbers+1) 반복 횟수 정함
    simple_password += random.choice(letters)
    hard_password += random.choice(letters)

for char in range(0,nr_symbols):
    simple_password += random.choice(symbols)
    hard_password += random.choice(symbols)

for char in range(0,nr_numbers):
    simple_password += random.choice(numbers)
    hard_password += random.choice(numbers)

print(simple_password)
print(hard_password)
random.shuffle(hard_password)

password = ""

for char in hard_password:
    password += char

print(f"Your password is: {password}")

