
def main() -> None:
    num: int = int(input("Enter your number for double: "))
    result: int = double_number(num)
    print(f"{num} * 2 = {result}")

def double_number(num: int) -> int:
    return num * 2

if __name__ == '__main__':
    main()