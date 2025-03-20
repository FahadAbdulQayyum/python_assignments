from time import sleep

def main() -> None:
    lift_off()

def lift_off():
    for i in range(10, 0, -1):
        print(i)
        sleep(2)
    print("Lift off!")

if __name__ == '__main__':
    main()