# l = [1,2,3,4,5]
# newl = list(map(lambda x : x ** 3, l))
# print(newl) #1,4,9,16,25

# def check_even(n):
#     return n % 2 == 0
# newl2 = list(filter(check_even, newl))
# print(newl2)
        # or,
# newl2 = list(filter(lambda x : x % 2 == 0, newl))
# print(newl2)

l = [1,2,3,4,5]
newl = list(map(lambda x : x ** 3, l))
# print(newl)

newl2 = list(filter(lambda x : x % 2 == 0, newl))
# print(newl2)