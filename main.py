student_dict = {
    "student": ["Natalia", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dictionery = {row.letter:row.code for (index, row) in data.iterrows()}

i = 0
name = input("Enter a Word: ")
name = list(name)
nato_phonetic_alphabet_list = []
for i in name:
#     nato_phonetic_alphabet_list = [value.title() for key,value in nato_phonetic_alphabet_dictionery.items() if i.upper() == key]
# print(nato_phonetic_alphabet_list)
    for key,value in nato_phonetic_alphabet_dictionery.items():
        if i.upper() == key:
            nato_phonetic_alphabet_list.append(value.title())
print(nato_phonetic_alphabet_list)