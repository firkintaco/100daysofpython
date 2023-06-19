rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_choice = random.randint(0, 2)

if choice == 0 and computer_choice == 2:
    print("User wins!")
elif choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif choice == 2 and computer_choice == 1:
    print("User wins!")
elif choice == computer_choice:
    print("It's a tie.")
elif computer_choice > choice:
    print("Computer wins!")
else:
    print("Invalid number")
choices = [rock, paper, scissors]
print(choices[choice])

print(f"Computer chose:\n{choices[computer_choice]}")

