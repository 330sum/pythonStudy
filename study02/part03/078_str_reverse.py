txt = 'abcdefghijk'
ret = txt[::-1]  # 거꾸로
print(ret)  # [출력] kjihgfedcba

ret = txt[::-2]  # 거꾸로 된 순서 + 홀수
print(ret)  # [출력] kigeca

ret = txt[-2::-2]  # 거꾸로 된 순서 + 홀수
print(ret)  # [출력] jhfdb
