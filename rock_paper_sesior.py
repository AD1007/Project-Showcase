import random

def play_round(Aneek, Bidisha):
    choices = ["rock", "paper", "scissors"]
    Aneek_choice = random.choice(choices)
    Bidisha_choice = random.choice(choices)

    if Aneek_choice == Bidisha_choice:
        return "tie"
    elif (Aneek_choice == "rock" and Bidisha_choice == "scissors") or \
         (Aneek_choice == "paper" and Bidisha_choice == "rock") or \
         (Aneek_choice == "scissors" and Bidisha_choice == "paper"):
        return Aneek
    else:
        return Bidisha

def play_match(Aneek, Bidisha, num_rounds):
    Aneek_wins = 0
    Bidisha_wins = 0

    for _ in range(num_rounds):
        round_winner = play_round(Aneek, Bidisha)

        if round_winner == Aneek:
            Aneek_wins += 1
        elif round_winner == Bidisha:
            Bidisha_wins += 1

    return Aneek_wins, Bidisha_wins

def main():
    bots = ["random", "sequential", "counter", "adaptive"]

    for bot in bots:
        Aneek_wins, Bidisha_wins = play_match("you", bot, 1000)
        win_percentage = Aneek_wins / (Aneek_wins + Bidisha_wins) * 100

        if win_percentage >= 60:
            print(f"You played against {bot} and won {win_percentage:.2f}% of the games.")
        else:
            print(f"You played against {bot} and won {win_percentage:.2f}% of the games. You need to win at least 60% to pass this challenge.")

if __name__ == "__main__":
    main()
