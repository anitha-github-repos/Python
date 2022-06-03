
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_word_dict = {word.letter:word.code for index, word in nato_data_frame.iterrows()}
print(nato_word_dict)

# user_input_word = input("please enter a word that needs a nato alphabet words?: ")
#
# user_word_list = [word.upper() for word in user_input_word]
# print(user_word_list)
# final_list = [nato_word_dict[key] for key in user_word_list]
# print(final_list)

is_any_errors = True

while is_any_errors:
    user_input_word = input("please enter a word that needs a nato alphabet words?: ")

    user_word_list = [word.upper() for word in user_input_word]
    try:
        final_list = [nato_word_dict[key] for key in user_word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(user_word_list)
        print(final_list)
        is_any_errors = False

