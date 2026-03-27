try:
    user_input = float(input(f"What is {equation}? "))

except ValueError:
    print("Invalid Input, please enter a number!")
    continue