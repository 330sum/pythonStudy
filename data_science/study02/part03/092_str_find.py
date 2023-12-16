txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)  # 22
print(offset2)  # 27
print(offset3)  # 38

# find(문자) - 인덱스 반환
# find(문자, 인덱스) - 인덱스 이후부터 조회해서 인덱스 반환
# 문자(열) 조회 불가능하면 -1 리턴