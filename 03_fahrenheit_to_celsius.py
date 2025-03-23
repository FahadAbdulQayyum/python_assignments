def main() -> None:
    fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
    toCelius: float = convertToCelius(fahrenheit)
    # print(str(fahrenheit)+'F' + ' -> ' + str(toCelius)+'C')
    print(f'{fahrenheit}F -> {toCelius:.2f}C')

def convertToCelius(data: float) -> float:
    convertedToCelius: float = (data - 32) * 5.0 / 9.0
    return convertedToCelius

if __name__ == '__main__':
    main()