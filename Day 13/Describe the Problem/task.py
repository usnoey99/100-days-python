def my_function():
    # for i in range(1, 20): error
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop iterates through numbers starting at 1 up to 20 (inclusive),
# assigning each value to the variable i one at a time.

# 2. When is the function meant to print "You got it"?
# The function prints "You got it" only when i equals 20 during the loop.

# 3. What are your assumptions about the value of i?
# i is an integer that increases step by step from 1 to 20.
# It takes every whole number value in that range, including 20.
