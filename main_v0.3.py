import random

# VARIABLES ================================================================================

# clarify my the lists for the numbers in the equation
numerator = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
denominator = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
operators = ["+", "-", "*", "/"]

# select a random number from the list
numerator_random = random.choice(numerator)
denominator_random = random.choice(numerator)
operators_random = random.choice(operators)

# bit out of place but it helps make the operators work properly
if op == "+":
    result = numerator_random + denominator_random
elif op == "-":
    result = numerator_random - denominator_random
elif op == "*":
    result = numerator_random * denominator_random
elif op == "/":
    result = numerator_random / denominator_random
# and finally put them together (change the + to a list that is chosen as random)
equation = f"{numerator_random} {operators_random} {denominator_random}"

# INSTRUCTIONS & START SECTION =============================================================

# used in roll it 13, this is for my instructions at the start of the game getting the users input
def yes_no(question):
    question = "- Do you want instructions? -"
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please Enter Yes Or No!")

# define the instructions for the start of the game
def instructions():
    print("""
==== Instructions ====

Your goal is simple, solve the equations given and collect points,
one correct gives one point and one wrong gives a negative point.
Good Luck!
    """)

# make a title to print at the start of every game
title = "=== BASIC MATH QUEST ==="
print(title)
print()

# executing the instructions and asking the user for an input (from yes_no func)
ask_instructions = yes_no('- Do you want instructions? - ')

# if the user has put yes or y then it will come back with instructions
if ask_instructions == "yes":
    instructions()

# ==============================================================================

