strdata = input('정렬할 문자열을 입력하세요: ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = ''.join(ret1)  # join(): 정렬한 결과인 리스트를 문자열로 생성
ret2 = ''.join(ret2)
print('오름차순 정렬된 문자열은 <' + ret1 + '>입니다.')
print('내림차순 정렬된 문자열은 <' + ret2 + '>입니다.')

print('===========================================')
strdata2 = 'qwertyuiop230909'
ret3 = ''.join(sorted(strdata2))
ret4 = ''.join(sorted(strdata2, reverse=True))
print(ret3, ret4)
