def main() -> None:
    num: float = float(input("Type a number to see its square: "))
    res: float = to_square(num)
    print(f"Square of {num} is {res}.")
def to_square(num: float) -> float:
    return num**2

if __name__ == '__main__':
    main()