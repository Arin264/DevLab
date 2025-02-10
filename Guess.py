import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # The number to guess is randomly chosen between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            user_guess = int(input("Make a guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")
    
# Run the game
guess_the_number()
