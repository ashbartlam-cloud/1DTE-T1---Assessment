import random
import math

# VARIABLES ================================================================================

error = "Not a valid input."
# some empty variables to be filled later in the game
user_points = 0
game_history = []

# clarify my the lists for the numbers in the equation
# easy difficulty
numerator_easy = [1, 3, 5, 7, 9]
denominator_easy = [2, 4, 6, 8, 10]
operators_easy = ["+", "-"]

# hard difficulty
numerator_hard = [1, 3, 5, 7, 9, 11]
denominator_hard = [2, 4, 6, 8, 10]
operators_hard = ["+", "-", "*", "/"]

# select a random number from the list
numerator_random_easy = random.choice(numerator_easy)
denominator_random_easy = random.choice(numerator_easy)
operators_random_easy = random.choice(operators_easy)

numerator_random_hard = random.choice(numerator_hard)
denominator_random_hard = random.choice(numerator_hard)
operators_random_hard = random.choice(operators_hard)

# and finally put them together (change the + to a list that is chosen as random)
equation_easy = f"{numerator_random_easy} {operators_random_easy} {denominator_random_easy}"
equation_hard = f"{numerator_random_hard} {operators_random_hard} {denominator_random_hard}"
# INSTRUCTIONS & START SECTION =============================================================

# used in roll it 13, this is for my instructions at the start of the game getting the users input
def yes_no(question):
    question = "- Do you want instructions? - "
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please Enter Yes Or No!")

def difficulty(question):
    question = "- Choose Difficulty EASY or HARD - "
    while True:
        response = input(question).lower()

        if response == "easy":
            return "easy"
        elif response == "hard":
            return "hard"
        else:
            print("Please enter a valid difficulty!")

# define the instructions for the start of the game
def instructions():
    print("""
==== Instructions ====

Your goal is simple, solve the equations given and collect points,
one correct gives one point and one wrong gives a negative point.
Good Luck!

Keys:
+ = Addition
- = Subtraction
* = Multiplicaton
/ = Division

If you would like to exit the game use '000' to end the game and view your history
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

# START OF GAME HERE ====================================================================
user_difficulty = difficulty("- Choose Difficulty EASY or HARD - ").lower()


if user_difficulty == "easy":

    while True:
        numerator_random = random.choice(numerator_easy)
        denominator_random = random.choice(denominator_easy)
        operators_random = random.choice(operators_easy)

        equation = f"{numerator_random} {operators_random} {denominator_random}"

        answer = eval(equation)
        user_input = float(input(f"What is {equation}? "))

        if user_input == answer:
            print("☑️Well Done, you got it correct!☑️")
            user_points += 1

            game_history.append(f"{equation} = ☑️ {answer}")

        elif user_input == 000:
            break

        elif user_input != answer:
            print(f"❌Sorry but that was incorrect, the correct answer was {answer}❌")
            user_points -= 1

            game_history.append(f"{equation} = ❌ {answer}")



elif user_difficulty == "hard":

    while True:
        numerator_random = random.choice(numerator_hard)
        denominator_random = random.choice(denominator_hard)
        operators_random = random.choice(operators_hard)

        equation = f"{numerator_random} {operators_random} {denominator_random}"

        answer = eval(equation)
        user_input = float(input(f"What is {equation}? "))

        if user_input == answer:
            print("☑️Well Done, you got it correct!☑️")
            user_points += 1

            game_history.append(f"{equation} = ☑️ {answer}")

        elif user_input == 000:
            break

        elif user_input != answer:
            print(f"❌Sorry but that was incorrect, the correct answer was {answer}❌")
            user_points -= 1

            game_history.append(f"{equation} = ❌ {answer}")
