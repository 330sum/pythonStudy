class MyClass:
    var = '안녕하세요'

    def sayHello(self):
        print(self.var)


obj = MyClass()  # MyClass 인스턴스 객체 생성
print(obj.var)  # [출력] 안녕하세요
obj.sayHello()  # [출력] 안녕하세요
