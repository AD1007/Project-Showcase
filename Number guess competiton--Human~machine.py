import random
import time

while True:
    try:
        # Get input from human player
        lower = int(input("Enter lower limit: "))
        upper = int(input("Enter upper limit: "))

        # Validate range
        if lower > upper:
            print("Lower limit cannot be greater than upper limit. Try again.")
            continue

        # Generate secret number
        secret_num = random.randint(lower, upper)

        # Set timeout for simultaneous guessing
        timeout = 10  # Adjust this value based on your preference

        # Get human guess with timeout
        try:
            human_guess = int(input("Enter your guess: "))
        except ValueError:
            human_guess = None

        # Get computer guess after timeout
        time.sleep(5)
        computer_guess = random.randint(lower, upper)

        # Check guesses and declare winner
        if human_guess is None:
            print("Human took too long! Computer wins!")
        elif human_guess == secret_num:
            print("Congratulations! You guessed the number!")
        elif computer_guess == secret_num:
            print("The computer guessed the number. Machines are taking over!")
        else:
            human_diff = abs(human_guess - secret_num)
            computer_diff = abs(computer_guess - secret_num)
            if human_diff < computer_diff:
                print("You win! You were closer to the secret number.")
            elif human_diff > computer_diff:
                print("The computer wins! It was closer to the secret number.")
            else:
                print("It's a tie! Both human and computer were equally close.")

        # Repeat game or quit
        choice = input("Play again? (y/n) ").lower()
        if choice not in ("y", "n"):
            print("Invalid input. Quitting game.")
            break
        elif choice == "n":
            break

    except ValueError:
        print("Invalid input. Please enter integers!")

