import pandas
data = pandas.read_csv("./nato_phonetic_alphabet.csv")


word = input("Enter a word: \n").upper()
word_dict = {row.letter:row.code for (index, row) in data.iterrows()}
output_list = [word_dict[letter] for letter in word]
print(output_list)
# {new_key:new_value for (index, row) in df.iterrows()}