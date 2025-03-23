def main() -> None:
    num1: int = int(input("Enter your first number: "))
    num2: int = int(input("Enter your second number: "))

    sum: int = num1 + num2

    print(num1, '+', num2, '=', sum)


if __name__ == '__main__':
    main()