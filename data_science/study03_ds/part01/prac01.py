# 아래의 문자를 딕셔너리 형태로 변경하기
# 1. 문자열을 ">" 문자로 나눕니다.(split)
# 2. 반복문으로 문자열을 나눠 만든 리스트를 순회합니다.(for)
# 3. 비어있는 문자일때는 건너뜁니다.
# 4. 비어있지 않다면 공백으로 나눕니다.(split)
# 5. 나눈 문자열로 지역과 지역번호를 구분해서 dict 에 넣어줍니다.
# 6. 딕셔너리를 출력해서 잘 만들어졌는지 확인해 봅니다.
phone = ">경기 031 >강원 033 >충남 041 >충북 043 >경북 054 >경남 055 >전남 061 >전북 063"

split = phone.split('>')
phone_list = list(split)

print(phone_list)

phone_dict = {}
for i in phone_list:
    i_split = i.split()
    if len(i_split) > 0:
        # print(i_split)
        key = i_split[0]
        val = i_split[1]
        phone_dict[key] = val
        print(key, val)

print(phone_dict)
