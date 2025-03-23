def main() -> None:
    print("Main...")
    fav_animal: str = str(input("What is favourite animal? "))
    bot(fav_animal)

def bot(fav: str) -> None:
    print("My favorite animal is also", fav+"!")

if __name__ == '__main__':
    main()