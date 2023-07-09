

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road.Where do you want to go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
  choice2 = input("Type 'swim' or 'wait'.\n").lower()
  if choice2 == 'wait':
    choice3 = input("Which door? Type 'red','yellow' or 'blue'.\n")
    if choice3 == 'red':
      print("Burned by fire.Game over")
    elif choice3 == 'blue':
      print("Eaten by beasts.Game over")
    elif choice3 == 'yellow':
      print("You win")
    else:
      print('Game over.')
  else:
    print('Game over')
else:
    print("Fall into a hole.Game over")
