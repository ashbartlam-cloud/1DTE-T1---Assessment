while True:
    try:
        user_input = float(input(f"What is {equation}? ")) #obviously equation doesnt exist
        break # this is to exit the loop if the user_input is invalid :/
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
