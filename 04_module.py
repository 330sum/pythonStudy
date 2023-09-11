# 7.1.2 모듈 불러오기
import diva

# diva 모듈을 이용한 song() 메서드 실행
diva.Singer.song("적외선카메라")

# Singer 클래스 사용
singer = diva.Singer()
print(singer.name)

# 7.1.3 특정함수나 클래스만 불러오기
# calculator 모듈의 add() 함수만 사용
from calculater import add

print(add(3, 9))

# 모듈의 모든 내용 가져오기
from calculater import *

print(add(4, 5))
print(mul(3, 4))
print(div(2, 2))
