## Project 7: Password Generator Python Project

def main() -> None:
    print("Welcome to Password Generator!")
    pass_length = int(input("Enter the length of the password: "))
    password = password_generator(pass_length)
    print(f"Your password is: {password}")

def password_generator(length: int) -> str:
    import random
    import string
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password
if __name__ == '__main__':
    main()