# def cube(x):
#     return x ** 3
# l = [1,2,3,4,5]
# newl = []
# for numbre in l:
#     newl.append(cube(numbre))
# print(newl)
        # or,
# newl = list(map(cube, l))
# print(newl)
        # or,
# newl = list(map(lambda x : x ** 3, l))
# print(newl)

# 1. Square of numbers
# numbers = [2, 4, 6, 8, 10]
# print("Square of numbers are : ", list(map(lambda x : x ** 2, numbers)))

# 2. Convert strings to uppercase
# names = ["devesh", "rahul", "amit"]
# capitalName = list(map(lambda x : x.upper(), names))
# print(capitalName)
                # or,
# def capital(x):
#         return x.upper()
# a = ["devesh","shubham","raghu"]
# capitalName = []
# for name in a:
#         capitalName.append(capital(name))
# print(capitalName)

# 3. Add 5 to each number
# numbers = [10, 20, 30, 40]
# newn = list(map(lambda x : x + 5, numbers))
# print(newn)

# 4. Convert Celsius to Fahrenheit
# celsius = [0, 20, 30, 40]
# fahrenheit = list(map(lambda c : (9 * c) / 5 + 32, celsius))
# print(fahrenheit)       

# 5. Find length of each word
# def count(text):
#         total = 0
#         for i in text:
#                 total += 1
#         return total    
# words = ["python", "java", "c"]
# length = []
# for item in words:
#         length.append(count(item))
# print(length)
        # or,
# def count(text):
#         return len(text)      
# words = ["python", "java", "c"]
# length = []
# for item in words:
#         value = length.append(count(item))
# print(length)
        # or,
# words = ["python", "java", "c"]
# length = list(map(lambda x : len(x), words))
# print(length)
        # or,
# words = ["python", "java", "c"]
# length = list(map(len, words))
# print(length)

# 6. Convert list of strings into integers
# numbers = ["10", "20", "30", "40"]
# print(numbers)
# string = list(map(int, numbers))
# print(string)

# 7. Multiply two lists element-wise
# list1 = [2, 3, 4]
# list2 = [5, 6, 7]
# total = list(map(lambda x,y : x * y, list1, list2))
# print(total)

# 8. Remove spaces from strings
# names = ["  Rahul ", " Amit  ", " Neha "]
# newl = list(map(lambda x : x.strip(), names))
# print(newl)

# 10. Extract first character from each word
# words = ["Python", "Java", "C++", "JavaScript"]
# newl = list(map(lambda x : x[0], words))
# print(newl)