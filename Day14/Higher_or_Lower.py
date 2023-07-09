import random
from art import logo
from art import vs
from game_data import data

def format_data(account):
    """Takes the account data and returns printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return  f"{account_name},{account_descr}, from {account_country}"

def check_answer(guess,account_follower1,account_follower2):
    """Take the  User guess and follower counts and return  if they got it right."""
    if account_follower1 > account_follower2:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_a:
      account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}. ")
    print(vs)
    print(f"Against B: {format_data(account_b)}. ")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    account_follower1 = account_a["follower_count"]
    account_follower2 = account_b["follower_count"]

    is_correct = check_answer(guess,account_follower1,account_follower2)

    if is_correct:
        score += 1
        print(f"You're right!Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry.that's wrong.Final score: {score}.")
