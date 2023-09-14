list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c']]
list1[0] = 6  # [6,2,3,4,5] 출력
print(list1)


def myfunc():
    print('안녕!')


list4 = [1, 2, myfunc]
list4[2]()  # '안녕!'가 출력됨
