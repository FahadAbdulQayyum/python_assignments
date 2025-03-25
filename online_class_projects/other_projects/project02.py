## Project 2: Guess the Number Game Python Project (computer)

import random

def main() -> None:
    user_guessing()
    computer_guessing(10)

def computer_guessing(x: int):
    low: int = 1
    high: int = x
    feedback: str = ''
    while feedback != 'c':
        guess: int = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)?? ").lower()
        if feedback == 'h':
            high = guess - 1
            print("Computer guessed higher!")
        elif feedback == 'l':
            low = guess + 1
            print("Computer guessed lower!")
    print("Computer guessed it right!")

def user_guessing():
    random: int = random_number(10)
    while True:
        guess: int = int(input("Guess the number: "))
        guessing_level(random, guess)
        if random == guess:
            print("You guessed it right!")
            break

def random_number(num: int) -> int:
    rnd: int = int(random.random() * num)
    return rnd

def guessing_level(random: int, guess: int) -> None:
    if random < guess:
        print("You guessed higher!")
    elif random > guess:
        print("You guessed lower!")

if __name__ == '__main__':
    main()