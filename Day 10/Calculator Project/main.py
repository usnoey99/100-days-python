from art import logo

# Definition of functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

print("\n" *3)
print(logo)
print("\n" *3)
newCalculated = True

def calculratur():
    firstNr = int(input("What's the first number? >> "))
    continueCalculated = True
    while continueCalculated:
        for symbol in operations:
            print(symbol, end=' ')
        operation_symbol = input("\nPick an operation >> ")
        nextNr = int(input("What's the next number? >> "))

        result = operations[operation_symbol](firstNr, nextNr)

        print(f"{firstNr} {operation_symbol} {nextNr} = {result}")
        print("\n")
        nextStep = input(f"Type 'y' to continue calculating with {result},"
                         f"or type 'n' to start a new calculation"
                         f"or type 'e' to end the calculation: ").lower()
        print("\n")

        if nextStep == "y":
            firstNr = result
            continue
        elif nextStep == "n":
            continueCalculated = False
            calculratur()
        else: # nextStep == "e"
            break

calculratur()