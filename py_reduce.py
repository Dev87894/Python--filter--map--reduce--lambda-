from functools import reduce
# l = [1,2,3,4,5]
# newl = list(map(lambda x : x ** 3, l))
# print(newl)
# newl2 = list(filter(lambda x : x % 2 == 0, newl))
# print(newl2)
# total = reduce(lambda x, y : x + y, pf.newl2)
# print(total)

# 3. Find the Maximum Number
# numbers = [45, 12, 78, 34, 89, 23]
# largest = reduce(lambda x, y : x if x > y else y, numbers)
# print(largest)

# 5. Concatenate All Strings
# words = ["Python", "is", "awesome"]
# s1 = reduce(lambda x, y : f"{x} {y}", words)
# print(s1)

# 6. Count Total Characters
# words = ["apple", "banana", "kiwi"]
# total = reduce(lambda x,y : x + len(y) , words, 0)
# print(total)

# 7. Find the Longest String
# words = ["cat", "elephant", "dog", "giraffe"]
# l = reduce(lambda x, y : x if len(x) > len(y) else y, words)
# print(l)

