class Add:
    def add(self, n1, n2):
        return n1 + n2


# class 자식클래스(부모클래스):
class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2


obj = Calculator()
print(obj.add(1, 2))
print(obj.sub(1, 2))
