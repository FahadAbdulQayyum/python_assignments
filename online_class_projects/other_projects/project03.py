## Project 3: Guess the Number Game Python Project (user)

import random

def main() -> None:
    user_guessing()

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