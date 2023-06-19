from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)
def caesar(text, shift, direction):
  result_text = ""
  for letter in text:
    if letter not in alphabet:
      result_text += letter
    else:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
      else:
        new_position = position - shift
      result_text += alphabet[new_position]

  print(f"The {direction}d text is {result_text}") 

def caesar_cipher():
  end_cipher = False
  while not end_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
    caesar(text, shift ,direction)
  
    end_game = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if end_game == "no":
      end_cipher = True
      print("Good Bye")

caesar_cipher()
  