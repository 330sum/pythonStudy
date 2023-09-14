def add_txt(t1, t2='파이썬'):
    print(t1 + ' : ' + t2)


add_txt('베스트')  # [출력] 베스트 : 파이썬
add_txt(t2='대한민국', t1='만세')  # [출력] 만세 : 대한민국


# 가변인자
def func1(*args):
    print(args)


# 미정 키워드 인자
def func2(width, height, **kwargs):
    print(kwargs)


func1()  # [출력] ()
func1(3, 5, 1, 5)  # [출력] (3, 5, 1, 5)
func2(10, 20)  # [출력] {}
func2(10, 20, depth=50, color='blue')  # [출력] {'depth': 50, 'color': 'blue'}
