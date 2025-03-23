round: int = 0
score: int = 0
exit: bool = False  # EXIT is initialized as False

def main() -> None:
    print("""
        Welcome to the High-Low Game!
      --------------------------------
    """)

    high_low()

def high_low() -> None:
    random_number: int = random_number_generator()
    
    # Declare EXIT as a global variable to modify it inside the function
    global exit
    
    while not exit:
        # Capture user input as a string
        your_guessed: str = input("Enter your number (Type 'exit' to exit the game): ")
        
        # Check if the user wants to exit
        if your_guessed.lower() == 'exit':
            exit = True  # Set EXIT to True to terminate the loop
            continue
        
        # Convert input to an integer and evaluate the guess
        try:
            evaluate_guess(random_number, int(your_guessed))
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")
    
    print(f"The computer's number was {random_number}")

def evaluate_guess(random_num: int, guessed_num: int) -> None:
    global score, round  # Declare SCORE and ROUND as global variables
    
    if random_num == guessed_num:
        result = "Congratulations! You guessed it right! The computer's number was " + str(random_num)
        score += 1
    else:
        result = "Sorry! You guessed it wrong."

    round += 1

    if guessed_num > random_num:
        comparison = "higher"
    else:
        comparison = "lower"

    print(f"""
    Round {round}
    Your number is {guessed_num}
    Do you think your number is higher or lower than the computer's?: {comparison}
    {result}
    Your score is now {score}
        """)


def random_number_generator() -> int:
    import random
    return random.randint(1, 100)
    

if __name__ == '__main__':
    main()












# # from typing import Union

# ROUND: int = 1
# SCORE: int = 0
# EXIT: bool = False

# def main() -> None:
#     print("""
#         Welcome to the High-Low Game!
#       --------------------------------
#     """)

#     high_low()

# def high_low() -> None:
#     random_number: int = random_number_generator()
#     while not EXIT:
#         # your_guessed: Union[int, str] = int(input("Enter your number: "))
#         your_guessed: str = str(input("Enter your number (Type 'exit' to exit the game):"))
#         if your_guessed.lower() == 'exit':
#             EXIT = False
#             continue
#         evaluate_guess(random_number, int(your_guessed))
#     print(random_number)

# def evaluate_guess(random_num: int, guessed_num: int) -> None:
#     if random_num == guessed_num:
#         result = "Congratulations! You guessed it right! The computer's number was" + str(random_num)
#     else:
#         result = "Sorry! You guessed it wrong."

#     SCORE=+1
#     ROUND=+1

#     if guessed_num > random_num:
#         comparison = "higher"
#     else:
#         comparison  = "lower"

#     print(f"""
#     Round {ROUND}
#     Your number is {guessed_num}
#     Do you think your number is higher or lower than the computer's?: {comparison}
#     {result}
#     Your score is now {SCORE}
#         """)


# def random_number_generator() -> int:
#     import random
#     return random.randint(1, 100)
    

# if __name__ == '__main__':
#     main()