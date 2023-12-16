x = 0
while x < 10:
    x = x + 1
    if x < 3:
        continue  # while 구문 처음으로 이동하여 반복문 계속
    print(x)
    if x > 7:
        break  # while 구문 탈출함
