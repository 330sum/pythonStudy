bnum = 0b11110000
bstr = '0b11110000'
onum = 0o360
ostr = '0o360'
hnum = 0xf0
hstr = '0xf0'
b1 = int(bnum)
b2 = int(bstr, 2)  # b2 = int(bstr, 0)로도 가능
o1 = int(onum)
o2 = int(ostr, 8)  # o2 = int(ostr, 0)로도 가능
h1 = int(hnum)
h2 = int(hstr, 16)  # h2 = int(hstr, 0)로도 가능
print(b1)
print(b2)
print(o1)
print(o2)
print(h1)
print(h2)

# 0b(2진수), 0o(8진수), 0x(16진수)가 붙은 숫자는 자동으로 인식하고 10진수로 변환하기 때문에, 두번째 인자 생략가능.
# 문자열인 경우, 두번째 인자 명시해야 함
# 두번째 인자를 0으로 지정하면, 첫번째 인자 문자열을 숫자로 변환하고 10진수로 변환한 결과를 리턴
