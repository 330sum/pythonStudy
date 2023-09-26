import inspect


def add_number(n1, n2):
    sum = n1 + n2
    return sum


def add_txt(t1, t2):
    print(t1 + t2)


ans = add_number(10, 15)
print(ans)
text1 = '대한민국'
text2 = '만세'
add_txt(text1, text2)

data = range(1, 11)


def average(data):
    """리스트의 값을 받아 평균을 구하는 함수"""
    avg = sum(data) / len(data)
    return avg


print(average(data))

# 도움말 보기
help(average)
print(average.__doc__)
# 소스코드 보기
source_code = inspect.getsource(average)
print(source_code)
