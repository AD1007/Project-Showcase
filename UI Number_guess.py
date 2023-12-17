import random
import tkinter as tk

# Define the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Define function to handle guess button click
def guess_button_click():
    try:
        # Get the user's guess
        guess = int(guess_entry.get())

        # Validate guess against range
        if Lower_input > Upper_input or guess < Lower_input or guess > Upper_input:
            message_label.config(text="Guess must be between {} and {}".format(Lower_input, Upper_input))
            return

        # Update tries and check guess
        global tries
        tries += 1
        if guess == Secret_num:
            message_label.config(text="Congratulations! You guessed the number in {} tries!".format(tries))
            guess_button.config(state="disabled")
        elif guess < Secret_num:
            message_label.config(text="Your guess is too low.")
        else:
            message_label.config(text="Your guess is too high.")
    except ValueError:
        message_label.config(text="Invalid guess. Please enter an integer.")

# Generate secret number
Lower_input = int(input("Enter lower limit: "))
Upper_input = int(input("Enter upper limit: "))
Secret_num = random.randint(Lower_input, Upper_input)

# Initialize tries
tries = 0

# Create UI elements
guess_entry = tk.Entry(root, width=10, borderwidth=5)
guess_button = tk.Button(root, text="Guess", command=guess_button_click)
message_label = tk.Label(root, text="")

# Arrange UI elements
guess_entry.pack(pady=10)
guess_button.pack()
message_label.pack()

# Run the main loop
root.mainloop()
