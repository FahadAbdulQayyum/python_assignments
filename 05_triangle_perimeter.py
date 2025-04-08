def main() -> None:
    side_1: float = float(input("What is the length of side 1? "))
    side_2: float = float(input("What is the length of side 2? "))
    side_3: float = float(input("What is the length of side 3? "))

    calculated: float = calculate_perimeter_of_triangle(side_1, side_2, side_3)

    print(f"{side_1} + {side_2} + {side_3} = {calculated}")

def calculate_perimeter_of_triangle(s1: float, s2: float, s3: float) -> float:
    return s1 + s2 + s3

if __name__ == '__main__':
    main()