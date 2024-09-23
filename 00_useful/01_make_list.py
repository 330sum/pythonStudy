def func1(input_string):
    # 문자열을 쉼표와 공백으로 나누고, 리스트로 변환
    return [item.strip() for item in input_string.split(',')]


input_string_1 = "a, b, c   , d"

result_1 = func1(input_string_1)
print(result_1)  # ['a', 'b', 'c', 'd']


# ===================================================================================================
def func2(str):
    return [f"#{item.strip()}" for item in str.split(',')]


print("222======================")
input_string_2 = "가, 나, 다   , 라"
result_2 = func2(input_string_2)
print(result_2)  # ['#가', '#나', '#다', '#라']
formatted_result_2 = ', '.join(result_2)  # 리스트를 문자열로 결합
print(formatted_result_2)  # #가, #나, #다, #라


# ===================================================================================================

def func3(str):
    return [f"{item.strip()}" for item in str.split(',')]


print("333======================")
input_string_3 = "가나다, 나나, 다,    라"
rs_3 = func3(input_string_3)
print(rs_3)  # ['가나다', '나나', '다', '라']
formatted_rs_3 = ', '.join(rs_3)
print(formatted_rs_3)  # 가나다, 나나, 다, 라


# ===================================================================================================
def func4(str):
    return [f"{{{item.strip()}}}" for item in str.split(',')]


print("444======================")
str_4 = "h, e, l   ,l ,o"
rs_4 = func4(str_4)
print(rs_4)  # ['{h}', '{e}', '{l}', '{l}', '{o}']
formatted_rs_4 = '.'.join(rs_4)
print(formatted_rs_4)  # {h}.{e}.{l}.{l}.{o}


# ===================================================================================================
def func5(str):
    return [f"#{{${item.strip()}}}" for item in str.split(',')]


str_5 = 'qty, price'
rs_5 = func5(str_5)
print(rs_5)  # ['#{$qty}', '#{$price}']
formatted_rs5 = ', '.join(rs_5)
print(formatted_rs5)  # #{$qty}, #{$price}
