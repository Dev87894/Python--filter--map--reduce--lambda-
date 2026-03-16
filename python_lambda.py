# def cube(x):
#     return x**3
# print(cube(10))
        # or,
# cube = lambda x: x**3
# print(cube(10))
        # or,
# def cube(fx, value):
#     return fx(value)
# print(cube(lambda x: x ** 3, 10))

# 1. Square a Number
# square = lambda x : x ** 2
# print(square(6))

# 2. Find the Larger Number
# largest = lambda x, y : x if x > y else "equal" if x == y else y
# print(largest(70,70))

# 3. Check Even or Odd
# check = lambda x : "even" if x % 2 == 0 else "odd"
# print(check(150))

# 4. Find String Length
# text = lambda x : len(x)
# print(text("devesh"))

# 5. Reverse a String
# text = lambda x : x[::-1]
# print(text("devesh"))

# 6. Sort a List of Tuples
# students = [
#     ("Rahul", 75),
#     ("Amit", 90),
#     ("Neha", 82),
#     ("Priya", 95)
# ]
# students.sort(key = lambda student : student[1])
# print(students)
            # or,
# students = [
#     ("Rahul", 75),
#     ("Amit", 90),
#     ("Neha", 82),
#     ("Priya", 95)
# ]
# def get_marks(student):
#     return student[1]
# students.sort(key = get_marks)
# print(students)

# 7. Filter Even Numbers
# numbers = [10, 15, 22, 31, 48, 57, 60]
# evenNo = lambda number : number if number % 2 == 0 else 
# print(evenNo(numbers[0]))