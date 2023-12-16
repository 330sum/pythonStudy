class MyClass:
    var = '안녕하세요!'

    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)  # [출력] 안녕
        print(self.var)  # [출력] 안녕하세요


obj = MyClass()
print(obj.var) # [출력] 안녕하세요
obj.sayHello()
# obj.param1
