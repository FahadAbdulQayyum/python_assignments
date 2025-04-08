def wow():
    raise FloatingPointError("You")
def wow1():
    raise FileNotFoundError("Aday!")
def test_it():
    try:
        a = 10
        if a > 9:
            wow1()
    except FloatingPointError as e:
        print(f"You bloody fool! {e}")
    except FileNotFoundError as e:
        print(f"Again, you bloody fool! {e}")
        
        if a > 9:
            wow()
    except FloatingPointError as e:
        print(f"You bloody fool! {e}")
    except FileNotFoundError as e:
        print(f"Again, you bloody fool! {e}")

test_it()
# # # # # # # # # # # # # # # # 

# def run_it():
#     try:
#         a = 10/0
#         print(a)
#     except ZeroDivisionError:
#         print("Can not be divided by zero")
#     finally:
#         print("Hope, you keep yourself motivate to go ahead.")

# run_it()

# # # # # # # # # # # # # # # # 

# my_obj: dict[str, str] = {
#     "name": "Fahad",
#     "age": "34"
# }

# print(type(my_obj))
# print(list(my_obj.keys())[0])

# # # # # # # # # # # # # # # # 

