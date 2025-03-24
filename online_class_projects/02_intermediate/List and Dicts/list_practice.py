from typing import Union

union_of_str_int_bool = Union[str, int, bool]

def main() -> None:
    list_practice: list[union_of_str_int_bool] = ["Hello", 3, True, 5, False, "World"]
    print(list_practice)
    print('length:', len(list_practice))

    options: str = str(input("""Enter an operation: 
        1. Access
        2. Modify
        3. Slice
            """))
    
    match(options):
        case "1":
            value: int = int(input("Enter the index to access: "))
            returned: union_of_str_int_bool = return_index_value(list_practice, value)
            print("returned...", returned, 'type:', type(returned))
        case "2":
            index: int = int(input("Enter the index to modify: "))
            value: union_of_str_int_bool = input("Enter the value to modify: ")
            returned: union_of_str_int_bool = return_modified_index_value(list_practice, index, value)
            print("returned with modified...", returned, 'type:', type(returned), 'List:', list_practice)
        case "3":
            first_index: int = int(input("Enter the first index to slice: "))
            last_index: int = int(input("Enter the last index to slice: "))
            returned: union_of_str_int_bool = return_range_index(list_practice, first_index, last_index)
            print("returned with range index...", returned, 'type:', type(returned), 'List:', list_practice)
        case _:
            print("Invalid option")

def return_range_index(arr: list[union_of_str_int_bool], start_index: int, end_index: int) -> union_of_str_int_bool:
    try:
        return [a for a in arr[start_index:end_index]] 
    except IndexError:
        return "Index out of range"
    
def return_modified_index_value(arr: list[union_of_str_int_bool], index: int, modified_value: int) -> union_of_str_int_bool:
    try:
        arr[index] = modified_value
        return arr[index] 
    except IndexError:
        return "Index out of range"

def return_index_value(arr: list[union_of_str_int_bool], index: int) -> union_of_str_int_bool:
    try:
        return arr[index]
    except IndexError:
        return "Index out of range"

if __name__ == '__main__':
    main()