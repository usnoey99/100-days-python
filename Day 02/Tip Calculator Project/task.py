print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10%, 12% or 15% "))
people = int(input("How many people to split the bill? "))
tip_percent = bill*(tip/100)
pay = (bill + tip_percent) / people
final_amount = round(pay,2)
print(f"Each person should pay {final_amount} $")


