tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])
# tuple[0] = 6 # 오류 발생

def myfunc():
    print('안녕!')


tuple4 = [1, 2, myfunc]
tuple4[2]()  # '안녕!'이 출력됨
