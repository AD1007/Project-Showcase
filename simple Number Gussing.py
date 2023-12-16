import random

while True:
    try:
        Lower_input = int(input("Lower Limit is:"))
        Upper_input = int(input("upper Limit is:"))
        if (Lower_input>Upper_input):
            print("Lower input can't be greater than upper input. Correct it again")
            continue
        break
    except ValueError:
        print("The input value isn't integers")

Secret_num = random.randint(Lower_input,Upper_input)

guess = None
tries = 0

while guess != Secret_num:
    try:    
        tries +=1
        guess = int(input(f"Guess the number in between the {Lower_input}  to {Upper_input}:"))
        if guess> Upper_input:
            print(f"Value exceeded the {Upper_input}. Put values lower than {Upper_input}")
        elif guess < Lower_input:
            print(f"Input is lower that {Lower_input}.Put values greater than {Lower_input}")
        if guess<Secret_num <=2*guess:
            print("You gussed it little lower")
        elif 2*guess < Secret_num <=3*guess:
            print("You gussed it too much low")
        elif 3*guess < Secret_num:
            print("Your gussed value is not even in the close range.Try harder")
        elif guess > Secret_num >= 2*guess:
            print("You gussed it little higher")
        elif 2*guess > Secret_num >= 3*guess:
            print("You gussed it too much low ")
        elif 3*guess < Secret_num:
            print("Your guessed value is not even in the close range.Try harder")
        else:
            print(f"Congratulations.Your guess, {guess}, is perfectly matches with our {Secret_num}, and you make it possible in {tries}")
        
            break    
    except ValueError:
        print(f"{guess} is not an integer")

