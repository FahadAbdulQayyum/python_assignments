# # # # # # # USING FOR LOOP # # # # # # #

import random

def main() -> None:
    N_NUMBERS: int = 10
    MIN_VALUE: int = 1
    MAX_VALUE: int = 100

    random: int = random_number(MAX_VALUE)
    num_array: list[int] = []
    for _ in range(MIN_VALUE, N_NUMBERS):
        random = random_number(MAX_VALUE)
        num_array.append(random)
    print(num_array)

def random_number(num: int) -> int:
    rnd: int = int(random.random() * num)
    return rnd

if __name__ == '__main__':
    main()


# # # # # # USING WHILE LOOP # # # # # #

# import random

# def main() -> None:
#     N_NUMBERS: int = 10
#     MIN_VALUE: int = 1
#     MAX_VALUE: int = 100

#     random: int = random_number(MAX_VALUE)
#     num_array: list[int] = []
#     count:int = 1
#     while count <= N_NUMBERS:
#         random = random_number(MAX_VALUE)
#         num_array.append(random)
#         print(num_array)
#         count+=1
 
# def random_number(num: int) -> int:
#     rnd: int = int(random.random() * num)
#     return rnd

# if __name__ == '__main__':
#     main()