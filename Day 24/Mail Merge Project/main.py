#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"
invite_list = []

with open("./Input/Names/invited_names.txt", mode="r") as name_list:
    for line in name_list:
        invite_list.append(line.strip())

with open("./Input/Letters/starting_letter.txt", mode="r") as basic_letter:
    letter = basic_letter.read()
    for name in invite_list:
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as ready_letter:
            ready_letter.write(letter.replace(PLACEHOLDER, name))
