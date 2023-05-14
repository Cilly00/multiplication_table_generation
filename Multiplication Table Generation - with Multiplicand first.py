welcome_user = input("Welcome to the Multiplication Tables Generator! Please enter your username. ") # Asks the user to enter their username.
number_chosen = int(input(f"Hello, {welcome_user}. Display a multiplication table of the number of your choice. ")) # Asks the user to enter a number they want to display table for.
confirmation = input(f"You have chosen {number_chosen} as your number of choice, is that correct? Confirm with yes or no. ").lower() # Asks the user if the number selected is correct.
if confirmation == "yes":  ## If confirmed - display the multiplication table of number selected.
    for i in range(1,13):
        print(i,'x', number_chosen, '=', number_chosen*i)
print(f"Thank you for using Cillein's Multiplication Table Generator, {welcome_user}. Come back soon!") # Displays a goodbye message, addressing user by their name.
if not confirmation == "yes": # If not confirmed - it will ask user to re-enter their number of choice.
    print("Please try again.")
    exit() # Program will exit once complete.
    