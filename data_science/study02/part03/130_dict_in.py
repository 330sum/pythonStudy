# 사전에 특정 키가 존재하는지 확인하기
names = {'Marry': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}
k = input('이름을 입력하세요: ')
if k in names:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.' % (k, names[k]))
else:
    print('자료에 <%s>인 이름이 존재하지 않습니다.' % k)

print('========================')

# 사전에 특정 값이 존재하는지 확인하기
if 2111 in names.values():
    print('주어진 값이 사전에 존재함')
else:
    print('주어진 값이 사전에 존재하지 않음')
