import random

def game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        user_choice = user_choice.strip().lower()  # Remove spaces and convert to lowercase

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper, or scissors.")#if user write something different than given, then it will inform also.
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}") #display the winning score of user and computer

        play_again = input("Do you want to play again? (yes/no): ") #asking to user if they wsnt to play or not
        if play_again.lower() != "yes":
            break

game()