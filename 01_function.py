# 5.1.1 타입 힌팅
# 단어 1개, 숫자 1개를 전달 받아서 단어의 길이와 숫자를 곱해서 반환한다.
def count_length(word: str, num: int) -> int:
    return len(word) * num


length = count_length("sumin", 3)
print(length)


# 5.1.2 함수를 변수처럼 전달하기
def add_with_transform(left, right, transform_func):
    tmp_val = transform_func(left) + transform_func(right)
    return transform_func(tmp_val)


def add_plus_1(number):
    return number + 1


# (2 + 1) + (3 + 1) + 1 = 8
ret_val = add_with_transform(2, 3, add_plus_1)
print(ret_val)
