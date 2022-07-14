import pandas



#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter your Name: ").upper()
user_input_list = []
for letter in user_input:
    user_input_list.append(phonetic_dict[letter])

print(user_input_list)


