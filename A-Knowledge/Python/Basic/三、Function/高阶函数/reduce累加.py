from functools import reduce

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = reduce(lambda x, y: x+y, list)

print(n)
