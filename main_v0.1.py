import random

# Used in roll it 13, this is for my instructions at the start of the game getting the users input
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

# Define the instructions for the start of the game
def instructions():
    print("""
==== Instructions ====

Your goal is simple, solve the equations given and collect points,
one correct gives one point and one wrong gives a negative point.
Good Luck!
    """)

# Make a title to print at the start of every game
title = "=== Basic Math Quest ==="
print(title)
print()

# Asking the user if they would like instructions and checking whether they said yes or no
ask_instructions = yes_no('- Do you want instructions? - ')

if ask_instructions == "yes":
    instructions()

# Checks the users input
if operators_random == "+":
    result = numerator_random + denominator_random
elif operators_random == "-":
    result = numerator_random - denominator_random
elif operators_random == "*":
    result = numerator_random * denominator_random
elif operators_random == "/":
    result = numerator_random / denominator_random
