## Project 4: Rock, paper, scissors Python Project

import random

def main() -> None:
    print("Welcome to Rock, Paper, Scissors game!")
    # choice: str = random.choice(["rock", "paper", "scissors"])
    choice: str = random.choice(["r", "p", "s"])

    print("Computer choice: ", choice)
    user_choice: str = input("Your choice: ").lower()

    if user_choice == choice:
        print("It's a tie!")
    elif user_choice == "rock" or user_choice == "r":
        if choice == "scissors" or choice == "s":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "paper" or user_choice == "p":
        if choice == "rock" or choice == "r":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "scissors" or user_choice == "s":
        if choice == "paper" or choice == "p":
            print("You win!")
        else:
            print("You lose!")  

if __name__ == '__main__':
    main()