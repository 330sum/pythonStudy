url = 'http://www.naver.com/news/today=20230919'
log = 'name:밤비 agd:29 sex:여자 nation:대한민국'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()  # 공백을 구분자로 사용
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s' % (d1, d2))
