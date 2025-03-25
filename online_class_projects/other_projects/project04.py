## Project 4: Rock, paper, scissors Python Project

import random

def main() -> None:
    print("Welcome to Rock, Paper, Scissors game!")
    choice: str = random.choice(["rock", "paper", "scissors"])

    print("Computer choice: ", choice)
    user_choice: str = input("Your choice: ").lower()

    if user_choice == choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "paper":
        if choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "scissors":
        if choice == "paper":
            print("You win!")
        else:
            print("You lose!")  

if __name__ == '__main__':
    main()