# 5.2 람다

def add_1(num):
    return num + 1


def add_1_oneline(num): return num + 1


# 함수를 변수처럼 할당하거나 전달할 수 있다.
# add_1() 함수와 add_plus_one 변수는 같은 개념임
add_plus_one = add_1

print(add_1(5))
print(add_plus_one(6))

lambda_plus_one = lambda x: x + 1

print(lambda_plus_one(7))

