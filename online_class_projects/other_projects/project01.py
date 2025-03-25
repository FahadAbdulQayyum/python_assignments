## Project 1: Mad libs Python Project

# Simple Mad Libs Game

def mad_libs() -> None:
    # Welcome message
    print("Welcome to Mad Libs!")
    print("Please provide the following words:\n")
    
    # Collect words from the user
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (past tense): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    
    # Create the story
    story = f"One {adjective1} day, a {noun1} {verb1} through the forest. " \
            f"It was a {adjective2} sight that surprised every {noun2} nearby!"
    
    # Display the result
    print("\nHere's your Mad Libs story:")
    print("-" * 30)
    print(story)
    print("-" * 30)

# Run the game
if __name__ == "__main__":
    mad_libs()
    
    # Ask if they want to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            print("\n" * 2)
            mad_libs()
        elif play_again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'")