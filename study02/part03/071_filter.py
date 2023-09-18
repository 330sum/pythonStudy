def getPrime(x):
    if x % 2 == 0:
        return

    for i in range(3, int(x / 2), 2):
        if x % i == 0:
            break
        else:
            return x


listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))

# filter(첫번째인자, 두번째인자)
# 첫번째 인자: 특정조건의 값을 추출하는 함수
# 두번째 인자: 리스트와 같은 반복 가능한 자료
