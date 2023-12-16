ch = input('문자를 1개 입력하세요: ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자: %s \t코드값: %d[%s]' % (ch, chv, hex(chv)))

# 문자를 1개 입력하세요: a
# 문자: a 	코드값: 97[0x61]
# 문자를 1개 입력하세요: 가
# 문자: 가 	코드값: 44032[0xac00]

# 내장함수 ord() - 아스키코드 값
