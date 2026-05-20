import pandas as pd

# Create a dictionary
nato_csv = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {letter: code for (letter, code) in zip(nato_csv["letter"], nato_csv["code"])}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

phonetic_code = [nato_dict[letter] for letter in user_input if letter in nato_dict]
print(phonetic_code)

