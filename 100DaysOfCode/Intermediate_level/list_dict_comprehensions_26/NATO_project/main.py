import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please Enter Your Name: ").upper()
name_list = [nato_dict[letter] for letter in name]
print(name_list)