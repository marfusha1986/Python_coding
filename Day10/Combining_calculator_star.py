#Calculator
from art import logo
print(logo)
#Add
def add(a,b):
    return a + b

#Subtraction
def sub(a,b):
    return a - b

#Multiply
def mult(a,b):
    return a * b

#Division
def div(a,b):
    return a / b

operations = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}
def calculator():
    num1 = float(input("What's the first number?:"))
    for symbol in operations:
     print(symbol)
    should_continue = True
    while should_continue:
        first_operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?:"))
        calculation_function1 = operations[first_operation_symbol]
        answer = calculation_function1(num1,num2)
        print(f"{num1} {first_operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

