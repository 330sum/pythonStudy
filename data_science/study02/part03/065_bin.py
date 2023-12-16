b1 = bin(97)  # b1은 문자열 '0b110000001'
b2 = bin(98)  # b2는 문자열 '0b110000010'
ret1 = b1 + b2
print(ret1)  # [출력] '0b1100000010b110000010'
a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b
print(bin(ret2))  # [출력] 0b11000011
