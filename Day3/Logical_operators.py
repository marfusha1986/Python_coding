print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
e = name1+name2
x = e.lower()
a1 = x.count("t")
a2 = x.count("r")
a3 = x.count("u")
a4 = x.count("e")
a5 = x.count("l")
a6 = x.count("o")
a7 = x.count("v")
a8 = x.count("e")

true = a1 + a2 + a3 + a4
love = a5 + a6 + a7 + a8
x = str(true) + str(love)
x1 = int(x)
if x1 < 10 or x1 > 90:
    print(f"Your score is {x1}, you go together like coke and mentos.")
elif x1 > 40 and x1 < 50:
    print(f"Your score is {x1}, you are alright together.")
else:
    print(f"Your score is {x1}.")


