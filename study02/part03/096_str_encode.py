u_txt = 'I love python'
b_txt = u_txt.encode()  # 73 32 109 111 118 101 32 112 121 116 104 111 110
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]  # I
ret2 = 'I' == b_txt[0]  # 73

print(ret1)  # True
print(ret2)  # False
