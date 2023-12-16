f = lambda x: x * x
args = [1, 2, 3, 4, 5]
ret = map(f, args)
print(list(ret))  # [1, 4, 9, 16, 25]
print(ret)  # <map object at 0x11f81b220>

f = lambda x, y: x * x + y
X = [1, 2, 3, 4, 5]
Y = [10, 9, 8, 7, 6]
ret = map(f, X, Y)
print(list(ret))  # [11, 13, 17, 23, 31]
