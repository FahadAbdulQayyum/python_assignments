def main() -> None:
    PROMPT: str = 'Tell me a joke?'
    JOKE: str = 'joke'
    SORRY: str = "Sorry, I'm here just for joke."

    do_you_want_joke: bool = PROMPT.strip().lower().__contains__('joke')

    if do_you_want_joke:
        joke: str = tell_me_a_joke(PROMPT, JOKE)
        print(joke)
    else:
        print(SORRY)

# def tell_me_a_joke(prompt:str, joke: Optional[str]="joke") -> str:
def tell_me_a_joke(prompt:str, joke:str = "joke") -> str:
    say_a_joke: str = "There was two people lost!"
    # say_a_joke: str = joke
    return say_a_joke

if __name__ == '__main__':
    main()