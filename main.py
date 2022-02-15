# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# data_dict = {letter:code for (letter,code) in data_file.iterrows()}

# data_frame = pandas.DataFrame(data_file, )

# data_final = data_frame.to_dict()
#Jprint(data_file)

data_final = {row.letter: row.code for (index, row) in data_file.iterrows()}

# form dictionary

#print(data_final)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

search_word = input("Enter a word : ").upper()

answer = []

answer = [data_final[letter] for letter in search_word]

#answer = []

#letter_list = list(search_word)

#for letter in letter_list:
#    answer.append(data_final.get(letter))

print(answer)
