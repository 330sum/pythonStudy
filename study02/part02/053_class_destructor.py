class MyClass:
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')


obj = MyClass()
del obj
# 인스턴스 객체를 메모리에서 제거하려면 del키워드를 사용
