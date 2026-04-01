import random
import math

# VARIABLES ================================================================================

error = "Not a valid input."
# some empty variables to be filled later in the game
game_history = []
user_input = 0

rounds = 0
played_rounds = 0
rounds_lost = 0
round_wins = 0

# clarify my the lists for the numbers in the equation
# easy difficulty
numerator_easy = [1, 3, 5, 7, 9, 11, 13]
denominator_easy = [2, 4, 6, 8, 10, 12, 14]
operators_easy = ["+", "-", "*"]

# select a random number from the list
numerator_random_easy = random.choice(numerator_easy)
denominator_random_easy = random.choice(numerator_easy)
operators_random_easy = random.choice(operators_easy)

# and finally put them together (change the + to a list that is chosen as random)
equation_easy = f"{numerator_random_easy} {operators_random_easy} {denominator_random_easy}"
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
while True:
    try:
        amount_of_rounds = int(input("- How many rounds would you like? - "))

        if amount_of_rounds > 1:
            if amount_of_rounds > 100:
                print("This is too many rounds, please enter an integer that is equal or less than 100")
            elif amount_of_rounds > 1:
                rounds = amount_of_rounds
                break
        elif amount_of_rounds <= 1:
            print("Please enter a integer over 1!")
    except ValueError:
        print("Please enter a valid integer!")

# difficulty is in here

while True:
    played_rounds += 1
    print(f"=== ROUND {played_rounds} ===")
    if played_rounds < rounds:
        numerator_random = random.choice(numerator_easy)
        denominator_random = random.choice(denominator_easy)
        operators_random = random.choice(operators_easy)

        equation = f"{numerator_random} {operators_random} {denominator_random}"

        answer = eval(equation)
        try:
            user_input = float(input(f"What is {equation}? "))

        except ValueError:
                print("Invalid Input, please enter a number!")
                continue


        if user_input == answer:
            print("☑️Well Done, you got it correct!☑️")
            round_wins += 1

            game_history.append(f"{equation} = ☑️ {answer}")

        elif user_input == 000:
            break

        elif user_input != answer:
            print(f"❌Sorry but that was incorrect, the correct answer was {answer}❌")
            rounds_lost += 1

            game_history.append(f"{equation} = ❌ {answer}")
    elif played_rounds >= rounds:
        break

# here is the history / end game section
print()

view_history = input("- Would you like to view your game history? - ").lower()

if view_history == "yes" or "y":
    print()
    print("=== Here is your game history: === \n", '\n '.join(game_history))
    try:
        rounds_won = round_wins - rounds_lost
        percent_won = rounds_won / round_wins * 100
        percent_lost = rounds_lost / round_wins * 100
        print("=== Game Statistics ===")
        print(f" Won: {percent_won:.2f}% \t"
              f" Lost: {percent_lost:.2f}% \t")
        print(f"You won {round_wins} rounds out of {played_rounds} rounds.")
    except ZeroDivisionError:
        print("You lost every round :/")
