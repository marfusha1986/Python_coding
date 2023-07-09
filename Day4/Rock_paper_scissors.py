import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#print(rock)

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#print(paper)

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#print(scissors)

game_images = [rock,paper,scissors]

print("What do you choose?")
user_choice=int(input("Type 0 for Rock,1for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number,you lose!")
else:
 print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose :",game_images[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("User wins!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")



