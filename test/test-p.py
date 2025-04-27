
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 
# # # # # # # # # # # # # # 



# # # # # # # # # # # # # # 

# class Human:
#     def __init__(self):
#         pass
#     def speak(self):
#         return "I'm Human!"
#     def walk(self):
#         return True

# class Fahad(Human):
#     def __init__(self):
#         super().__init__()
#     def speak(self):
#         return "I'm Fahad!"
#     def walk(self):
#         return True

# class Moza(Human):
#     def __init__(self):
#         super().__init__()
#     def speak(self):
#         return "I'm Moza!"
#     def walk(self):
#         return False

# moza = Moza()
# spk = moza.speak()
# wlk = moza.walk()
# # print(wlk, spk)
# print(f"{wlk} - {spk}")

# fahad = Fahad()
# spk = fahad.speak()
# fhd = fahad.walk()
# # print(fhd, spk)
# print(f"{fhd} - {spk}")

# # # # # # # # # # # # # # 

# class ABC:
#     def __init__(self):
#         pass

#     def func(self):  # Add 'self' as the first parameter
#         print("why not!")

#     def two(self):  # Add 'self' as the first parameter
#         print("twoness!")

# # Create an instance of the class
# abc = ABC()

# # Call the instance methods
# abc.func()  # Output: why not!
# abc.two()   # Output: twoness!


# class ABC:
#     def __init__(self):
#         pass
#     def func(self):
#         print("why not!")
#     def two(self):
#         print("twoness!")

# abc = ABC()
# abc.two()

# # # # # # # # # # # # # # 

# def hell():
#     print("****")
#     def fire():
#         print("May Allah keep you safe here!")
#     return fire()

# # Call hell(), which internally calls fire()
# hell()
# # a = hexll()
# # print(a())
# # a.fire()
# # # # # # # # # # # # # # 

# def hell():
#     def fire():
#         print("May Allah keep you safe here!")
#     fire()  # Call fire() inside hell()

# # Call hell(), which internally calls fire()
# hell()

# # # # # # # # # # # # # # 

# def hell():
#     def fire():
#         print("May Allah keep you save here!")
#     # return fire()
#     fire()

# # hell().fire()
# hell()()
# # a = hell()()
# # print(a)
# # # # # # # # # # # # # # 

# gen = (x for x in range(10))

# # print(next(gen))

# for v in gen:
#     print(v)

# # # # # # # # # # # # # # 

# def my_func():
#     yield 1
#     yield 4
#     yield 9
#     yield 0

# gen = my_func()

# print('- gen -', next(gen))

# for v in gen:
#     print('- v -', v)

# # # # # # # # # # # # # # 

# my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}

# def my_func(**my_dict):
#     print(my_dict)

# my_func(**my_dict)

# # # # # # # # # # # # # # 

# def posFun(x, y, /, z):
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(1, 2, z=3)

# # uncomment to see error
# posFun(x=1, y=2, z=3)

# # # # # # # # # # # # # # 

# import numpy as np
# print(np.array([1, 2, 3, 4]))

# # # # # # # # # # # # # # 

# import requests

# response = requests.get("https://fakestoreapi.com/products/1")
# print('- status_code -', response.status_code)
# print('- json -', response.json())
# print('- content -', response.content)
# print('- text -', response.text)
# print('- headers -', response.headers)

# # # # # # # # # # # # # # 

# from moduel import add

# print(f"""
# - Add -
#       {add(3, 10)}
# """)

# # # # # # # # # # # # # # 

# import gc
# gc.collect()
# print(gc.get_count())

# my_set: frozenset = {"Fahad", 27, "Software Engineer"}
# print(frozenset(my_set))
# my_set.add("Mand")
# print(my_set)

# # # # # # # # # # # # # # 

# my_name: str = "Fahad"
# print(hash(my_name))
# print(my_name.__hash__())

# # # # # # # # # # # # # # 

# my_set: set = {1, 2, 3}

# try:
#     # my_set.remove(4) # pops up the error of '4' not found and causes crash
#     my_set.discard(4) # use 'discard' instead which does not crash
# except Exception as e:
#     print(f"Error as {e}")

# print(my_set)

# # # # # # # # # # # # # # 

# obj: dict = {'name': 'Fahad', 'age': 28, 'profession': 'Software Engineer'}

# print(list(obj.keys())[1])
# print([[k, v] for v, k in obj.items()]) # Working
# print(obj.get('namey', 'Not Found - 404'))
# print([[k, v] for (v, k) in obj]) # Not working
# print([[k, v] for (k, v) in obj])
# print([[k, v] for k, v in obj])
# print([[k, v] for k, v in obj.items()]) # Working

# # # # # # # # # # # # # # 

# Words counter

# sentence = """
# **Projected Economy Size of AI:**

# The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

# 1. **Global AI Market Size:**
# 	* By 2025: $190 billion (Source: MarketsandMarkets)
# 	* By 2030: $1.5 trillion (Source: PwC)
# 2. **AI-Driven Economic Growth:**
# 	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
# 	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
# 3. **AI-Generated Revenue:**
# 	* By 2025: AI is expected to generate $15.7 trillion in revenue (Source: IDC)
# 	* By 2030: AI is expected to generate $33.5 trillion in revenue (Source: McKinsey)
# 4. **Job Market Impact:**
# 	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
# 	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

# **Industry-Specific Projections:**

# 1. **Healthcare:**
# 	* By 2025: AI is expected to generate $150 billion in revenue (Source: MarketsandMarkets)
# 2. **Financial Services:**
# 	* By 2025: AI is expected to generate $100 billion in revenue (Source: Accenture)
# 3. **Manufacturing:**
# 	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
# 4. **Transportation:**
# 	* By 2025: AI is expected to generate $20 billion in revenue (Source: MarketsandMarkets)

# **Regional Projections:**

# 1. **North America:**
# 	* By 2025: AI is expected to generate $100 billion in revenue (Source: MarketsandMarkets)
# 2. **Europe:**
# 	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
# 3. **Asia-Pacific:**
# 	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

# Note: These projections are based on various assumptions, including the pace of AI development, adoption"""

# words = sentence.split()
# words_count = {}

# for word in words:
#     if word in words_count:
#         words_count[word] += 1
#     else:
#         words_count[word] = 1

# print(f'...word_count...! {words_count}')

# # # # # # # # # # # # # # 

# info: dict = {'name': 'Fahad', 'age': 27, 'city': 'Quetta'}

# print([[k, v] for k, v in info.items()])
# print([tuple([k, v]) for k, v in info.items()])

# sqr: list = [i*2 for i in ["wow", "lets", "go", "there"] if len(i) > 3]
# print(sqr)

# # # # # # # # # # # # # # 

# a: str = "Where are you guys, come on you stupid? There are some other crazy people"
# b: str = "Where are you guys, come on you stupid? There are some other crazy people"

# print(a is b)
# print([i for i in dir(str) if '__' not in i])
# print([i for i in dir(int) if '_' not in i])

# arr: list[int] = [3,4,5,2,0,8]
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)

# arr: list[str] = ["welcomeee", "two", "karachi", "2015", "superhit"]
# arr.sort(key=len)
# print(arr)
# arr.sort(key=lambda k: k[-2])
# print(arr)

# wow_name: str = "Where are you all?"
# # print(wow_name.count('e'))
# print(wow_name.count('a'))


# print(r'How are you, bro?')

# my_string: str = ", "

# print(my_string.join(["Fahad", "Aftab", "Barkat"])+'!')

# print('-'.join("Balochistan".upper()))

# wow_name: str = "Where are you all?"

# # print(wow_name.find("are"))
# print(wow_name.find("Where"))

# # # # # # # # # # # # # # 

# import keyword
# print(keyword.kwlist)

# from keyword import kwlist
# print(kwlist)

# # # # # # # # # # # # # # 

# data: list = [1,2,3]
# if n := len(data):
#     print(f"Yes, it's {n}")

# # # # # # # # # # # # # # 

# print("Chone Waja, tao?")

# # # # # # # # # # # # # # 

# x: int =

# # # # # # # # # # # # # # 
