from typing import List, Dict

def main() -> None:
    user_info: List[Dict[str, int]] = []
    for a in range(1, 4):
        # friend_name: str = str(input("Enter you friend's name: "))
        friend_name: str = str(input(f"Enter your {a} friend's name: "))
        # friend_age: int = int(input("Enter you friend's age: "))
        friend_age: int = int(input(f"Enter your {a} friend's age: "))
        friend: Dict[str, int] = {friend_name: friend_age}
        user_info.append(friend)
        
    for user_dict in user_info:
        for name, age in user_dict.items():
            print(f"{name.capitalize()}'s age is {age}.")

if __name__ == '__main__':
    main()