param = 10
strdata = '전역변수'


def func1():
    strdata = '지역변수'
    print(strdata)


def func2(param):
    param = 1


def func3():
    global param
    param = 50


func1()  # [출력] 지역변수
print(strdata)  # [출력] 전역변수
print(param)  # [출력] 10
func2(param)
print(param)  # [출력] 10
func3()
print(param)  # [출력] 50
