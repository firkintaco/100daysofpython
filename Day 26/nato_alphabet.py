import pandas
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

valid_word = False
while not valid_word:
    try:
        word = input("Enter a word: \n").upper()
        word_dict = {row.letter:row.code for (index, row) in data.iterrows()}
        output_list = [word_dict[letter] for letter in word]
        print(output_list)
        valid_word = True
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        valid_word = False
# {new_key:new_value for (index, row) in df.iterrows()}