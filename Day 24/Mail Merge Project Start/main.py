#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
formatted_names = []
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        name = name.replace("\n", "")
        formatted_names.append(name)


# with open("./Input/Letters/starting_letter.txt") as file:
#     letter = file.read()
#     new_letter = letter.replace("[name]", "Kimmo")
#     print(new_letter)

for name in formatted_names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        lines = letter.read()
        formatted_letter = lines.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as output:
            output.write(formatted_letter)