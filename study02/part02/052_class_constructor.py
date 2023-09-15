class MyClass:
    def __init__(self):
        self.var = '안녕하세요!'
        print('MyClass 인스턴스 객체가 생성되었습니다')


obj = MyClass()  # [출력] MyClass 인스턴스 객체가 생성되었습니다
print(obj.var)  # [출력] 안녕하세요!


class MyClass2:
    def __init__(self, txt):
        self.var = txt
        print('생성자 인자로 전달받은 값은 <' + self.var + '> 입니다')


obj2 = MyClass2('밤비')
# obj3 = MyClass2() # 인자를 입력하지 않으면, 오류 발생
