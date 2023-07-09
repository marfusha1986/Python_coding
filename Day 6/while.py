#** Reeborg World

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def move_on():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     move_on()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

#***at_goal condition
#  while not at_goal:
#     move_on()


 #** The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.

# while not at_goal():
#     if wall_in_front():
#         move_on()
#     else:
#         move()

#The position, the height and the number of hurdles changes each time this world is reloaded.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def move_on():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
# while not at_goal():
#     if wall_in_front():
#         move_on():
#     else:move()

#******** Come back 15th day and rewrite again*****
#Write a program using an if/elif/else statement so Reeborg can find the exit.
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can,
# going straight ahead if it can’t turn right, or turning left as a last resort.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear:
#        turn_right()
#        move()
#     elif front_is_clear:
#         move()
#     else:
#         turn_left()
#
