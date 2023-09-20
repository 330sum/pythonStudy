val = input('문자 코드값을 입력하세요: ')
val = int(val)

try:
    ch = chr(val)
    print('코드값: %d[%s], 문자:%s' % (val, hex(val), ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 존재하지 않습니다!' % val)

# 내장함수 chr() - 숫자(코드값) 넣으면 문자 반환
