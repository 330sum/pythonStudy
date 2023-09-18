txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'  # 공백 포함되면 문자열 아님
txt4 = '3PO'  # 숫자 포함되면 문자열 아님
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)  # True
print(ret2)  # True
print(ret3)  # False
print(ret4)  # False
