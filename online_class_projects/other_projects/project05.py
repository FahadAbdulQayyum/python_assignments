## Project 5: Hangman Python Project

import random
import string
from words import wordss

def main() -> None:
    print("Welcome to Hangman Game!")
    # user_input = input('Type something:')
    hangman(10)

def hangman(lives: int):
    word: str = get_valid_word(wordss)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and lives:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f'You have {lives} lives left.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You guessed the word {word}!")
        
def get_valid_word(words: list[str]) -> str:
    word: str = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

if __name__ == '__main__':
    main()
