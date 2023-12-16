class Add:
    def add(self, n1, n2):
        return n1 + n2


class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2


class Test:
    def sub(self, n1, n2):
        return n1 - n2 - n2


# class 자식클래스(부모클래스1, 부모클래스2):
class Calculator(Add, Multiply, Test):
    def sub(self, n1, n2):
        return n1 - n2


obj = Calculator()
print(obj.add(1, 2))
print(obj.multiply(3, 2))
print(obj.sub(1, 2))  # Test 클래스(부모)랑 Calculator 클래스(자삭)에 메서드명이 동일하면, 자식클래스꺼 사용
