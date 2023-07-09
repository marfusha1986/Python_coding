import random

names_string =input("Give me everybody's names,separated by a comma.")
names=names_string.split(", ")
print(len(names))

num_items = len(names)
rand = random.randint(0, num_items-1)
# print(rand)
person_who_will_pay = names[rand]
print(person_who_will_pay+" is going to buy the meal today.")

