# 6.1 클래스
# 파스칼 케이스
class MyFirstClass:
    pass


# 6.2 클래스 변수와 인스턴스 변수
class Diva:
    # 클래스 변수 : 클래스 모두가 공유하는 변수
    version = "v3"

    def __init__(self, name="Diva"):
        # 인스턴스 변수
        self.name = name


# 클래스 변수 사용
diva1 = Diva()
diva2 = Diva("sumin")


def print_diva_info(diva):
    print("===")
    print("Name: ", diva.name)
    print("Version: ", diva.version)


print_diva_info(diva1)
print_diva_info(diva2)

# 클래스 변수의 변경
# Diva 클래스를 직접 수정한다는 것에 주의!
Diva.version = "v4"

print_diva_info(diva1)
print_diva_info(diva2)
print("==============")


# 6.3 클래스 메서드
# 클래스 내부의 함수는 관례적으로 메서드라고 한다.
# 함수와 달리, 클래스 메서드의 첫번째 파라미터는 언제나 클래스 자신을 참조하는 변수인 self로 지정해야 한다.

# 클래스에 메서드 추가
class Diva:
    # 클래스 변수
    version = "v3"

    def __init__(self, name="Diva"):
        # 인스턴스 변수
        self.name = name

    def song(self, title="song"):
        print(self.name + " sing the " + title)

    def medley(self):
        self.song()
        self.song("second song")
        self.song("third song")


# song()과 medley() 메서드 실행
voice_diva = Diva("Bambi")
voice_diva.song()
voice_diva.song("World is Mine")
voice_diva.medley()
print("==============")

# 클래스 메서드에 전달하는 첫번째 파라미터
Diva.song(voice_diva, "Tell your world")


# 인스턴스가 아니라, 클래스에서 직접 메서드를 호출함.
# self 자리에 Diva 인스턴스를 전달하면 해당 인스턴스로 메서드를 호출한 것처럼 작동.
# 인스턴스를 생성하지 않고도 해당 클래스의 메서드를 호출하도록 만들 수 있음 (self를 메서드의 파라미터로 추가하지 않으면 됨)

# self를 메서드의 파라미터로 추가하지 않음
class Calculater:
    def adder(l, r):
        print(l + r)


Calculater.adder(3, 9)


# 6.4 상속
class Sumin(Diva):
    def __init__(self, module="class uniform"):
        self.module = module
        # 슈퍼클래스를 초기화하지 않으면
        # 슈퍼클래스에서 초기화 & 할당되는 name 변수를 사용할 수 없음
        super().__init__("sumin")

    def dance(self):
        print("Dancing!")


park = Sumin()
print(park.module)
print(park.version)
print(park.name)
park.dance()
park.song("Hello, world")


# 서브클래스를 만들 때, 슈퍼클래스 자리에 여러클래스를 넣어서 다중 상속할 수 있음
# 이때, 서브클래스에 없는 변수나 메서드 등을 참조하려면, 슈퍼클래스가 할당된 순서대로 왼쪽부터 깊이 우선탐색으로 변수, 메서드를 찾음


# 6.5 덕 타이핑
# 오리처럼 행동하고, 오리처럼 날고, 오리처럼 소리내면 오리다
# 인터페이스 등의 개념 없이도 해당 이름의 변수, 메서드가 있으면 그냥 호출 할 수 있다라는 의미
class Cat:
    def sound(self):
        print("냐옹")


class Dog:
    def sound(self):
        print("멍멍")


cat = Cat()
dog = Dog()

animals = [cat, dog]

for animal in animals:
    animal.sound()