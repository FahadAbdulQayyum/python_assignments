## Project 5: Hangman Python Project

import random
import string
from words import wordss

def main() -> None:
    print("Welcome to Hangman Game!")
    # user_input = input('Type something:')
    hangman()

def hangman():
    word: str = get_valid_word(wordss)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

def get_valid_word(words: list[str]) -> str:
    word: str = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

if __name__ == '__main__':
    main()
