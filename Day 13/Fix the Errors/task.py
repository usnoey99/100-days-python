try:
    age = int(input("How old are you?"))

    if age > 18:
        # Fix 1: Proper indentation
        # Fix 2: Use f-string to display the actual value of age
        print(f"You can drive at age {age}.")
    else:
        print("You are too young to drive.")

# Catch error if input is not a number
except ValueError:
    print("Please enter a valid number.")