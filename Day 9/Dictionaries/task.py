# Lisitng dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


# retrieve an item from the dictionary
print(programming_dictionary["Bug"]) # type keyname not index number

# Add in dictionary
programming_dictionary["Loop"] = "The action of doing somthing over and over again."

print(programming_dictionary)


# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) # keys are printed
    print(programming_dictionary[thing]) # to get the values