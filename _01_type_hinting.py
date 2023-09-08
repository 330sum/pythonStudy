# 타입 힌팅
# 단어 1개, 숫자 1개를 전달 받아서 단어의 길이와 숫자를 곱해서 반환한다.
def count_length(word: str, num: int) -> int:
    return len(word) * num


length = count_length("sumin", 3)
print(length)
