def main() -> None:
    # x = 3.1415926 
    # print(f"{x:.2f}")
    weight_on_earth: float = float(input("Enter your weight on Earth: "))
    print(f"Your weight on Earth is {weight_on_earth:.2f} kg")
    weight_on_mercury(weight_on_earth)
    weight_on_venus(weight_on_earth)
    weight_on_mars(weight_on_earth)
    weight_on_jupiter(weight_on_earth)
    weight_on_saturn(weight_on_earth)
    weight_on_uranus(weight_on_earth)
    weight_on_neptune(weight_on_earth)

def weight_on_mercury(weight_on_earth: float) -> None:
    print(f"Weight on Mercury: {weight_on_earth * 0.376:.2f} kg")

def weight_on_venus(weight_on_earth: float) -> None:
    print(f"Weight on Venus: {weight_on_earth * 0.889:.2f} kg")

def weight_on_mars(weight_on_earth: float) -> None:
    print(f"Weight on Mars: {weight_on_earth * 0.378:.2f} kg")

def weight_on_jupiter(weight_on_earth: float) -> None:
    print(f"Weight on Jupiter: {weight_on_earth * 0.236:.2f} kg")

def weight_on_saturn(weight_on_earth: float) -> None:
    print(f"Weight on Jupiter: {weight_on_earth * 0.1081:.2f} kg")

def weight_on_uranus(weight_on_earth: float) -> None:
    print(f"Weight on Uranis: {weight_on_earth * 0.815:.2f} kg")

def weight_on_neptune(weight_on_earth: float) -> None:
    print(f"Weight on Neptune: {weight_on_earth * 0.114:.2f} kg")


if __name__ == '__main__':
    main()