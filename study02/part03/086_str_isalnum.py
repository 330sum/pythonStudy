txt1 = '안녕하세요?'
txt2 = '1. Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1)  # False - ? 있어서 안됨
print(ret2)  # False - .(마침표) -(하이픈) 있어서 안됨
print(ret3)  # True
