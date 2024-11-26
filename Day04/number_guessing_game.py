# That's a number guessing game
import random

def get_user_input(prompt):
    """Get input from the user and handle special commands."""
    user_input = input(prompt)
    if user_input.lower() == "x":
        print("Exiting the game. Goodbye!")
        exit()
    elif user_input.lower() == "n":
        print("Leaving the current game.")
        return "new_game"
    elif user_input.lower() == "s":
        return "show"
    return user_input

def play_game():
    """Play one round of the number guessing game."""
    number = random.randint(1, 20)
    attempts = 0
    print("I've picked a number between 1 and 20. Try to guess it!")
    
    while True:
        user_input = get_user_input("Enter your guess: ")

        if user_input == "show":
            print(f"The hidden number is: {number}")
            continue
        
        try:
            guess = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        attempts += 1
        if guess < number:
            print("Too small.")
        elif guess > number:
            print("Too big.")
        else:
            print(f"Exactly! You are right! It took you {attempts} guesses.")
            break

def main():
    """Main function to manage the game flow."""
    print("Welcome to the Number Guessing Game!")
    while True:
        result = play_game()
        if result == "new_game":
            continue
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()


     

