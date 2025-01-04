import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.number = None
        self.attempts = 0

        # GUI Elements
        self.label = tk.Label(root, text="I've picked a number between 1 and 20. Try to guess it!", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12))
        self.submit_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show Number", command=self.show_number, font=("Helvetica", 12))
        self.show_button.pack(pady=5)

        self.new_game_button = tk.Button(root, text="New Game", command=self.start_new_game, font=("Helvetica", 12))
        self.new_game_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.start_new_game()

    def start_new_game(self):
        """Start a new game by resetting values."""
        self.number = random.randint(1, 20)
        self.attempts = 0
        self.result_label.config(text="")
        self.label.config(text="I've picked a number between 1 and 20. Try to guess it!")
        self.entry.delete(0, tk.END)

    def check_guess(self):
        """Check the user's guess."""
        user_input = self.entry.get()
        if not user_input:
            self.result_label.config(text="Please enter a number.")
            return

        try:
            guess = int(user_input)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")
            return

        self.attempts += 1
        if guess < self.number:
            self.result_label.config(text="Too small.")
        elif guess > self.number:
            self.result_label.config(text="Too big.")
        else:
            self.result_label.config(text=f"Exactly! You are right! It took you {self.attempts} guesses.")
            self.label.config(text="Game over! Start a new game or close the window.")

    def show_number(self):
        """Show the hidden number."""
        self.result_label.config(text=f"The hidden number is: {self.number}")

# Create the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
