range1 = range(10)
range2 = range(10, 20)
print(list(range1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range2))  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

ret = 0
for i in range(10):
    ret += (i + 1)
print(ret)  # 55
