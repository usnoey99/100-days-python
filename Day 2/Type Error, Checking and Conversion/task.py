from operator import length_hint

len("12345")
print(type("Hello"))
print(type(1234))
print(type(3.14519))
print(type(False))

# name_of_user = input("Enter your name") #Type str
# length_of_user = len(name_of_user) #Type int
# print("Number of letters in your name: " + str(length_of_user))

print("Number of letters in your name: " + str(len(input("Enter your name"))))