import pandas as pd
import numpy as np

# 1. 그룹화하기
# 1-1. 날짜 형식을 계산할 수 있는 타입으로 바꾸기
dummy_data = pd.read_csv("/Users/superstar_park/PycharmProjects/source/ch14/examples/dummy.csv")

# 이 행으로 yyyy-mm-dd 형식의 문자열을 팬더스가 계산할 수 있는 datetime 타입으로 만들어준다.
dummy_data["df_date"] = pd.to_datetime(dummy_data["date"])
print(dummy_data.head())

print("==========================================")
# 1-2. groupby() 예제
by_contry = dummy_data.groupby("contry")
print(by_contry)

print("==========================================")
# 1-3. count()로 특정 열 값이 있는 행 개수 구하기
print(by_contry.count().head())

print("==========================================")
# 1-4. size()로 특정 열 값으로 그룹화한 행 개수 구하기
print(by_contry.size().head())

print("==========================================")
# 1-5. 나라별 각 열의 최댓값
print(by_contry.max().head())
print(by_contry.min().head())

print("==========================================")
# 1-7. describe()를 다른 데이터에 실행하기
print(by_contry.describe().head())

print("==========================================")
# 1-8. get_group()에 South Korea를 설정해 실행하기
print(by_contry.get_group('South Korea'))

# 2. agg()와 apply()함수로 데이터 가공하기
print("-----------------------------------------")
# 2-1. 딕셔너리 타입을 사용하는 agg() 예제
print(
    by_contry.agg(
        {
            "level":
                [
                    ("합계", np.sum),
                    np.mean,
                ]
        }
    )
)

print("-----------------------------------------")
# 2-2. 나라별로 level 열의 중간값(median) 구하기
print(
    by_contry.agg(
        {
            "level":
                [
                    np.size, np.median
                ]
        }
    )
)

print("-----------------------------------------")


# 2-3. 나라별 level의 제곱 합 구하기
def sum_of_pow(s: pd.core.series.Series):
    return sum([i ** 2 for i in s])


print(by_contry.agg({"level": [sum_of_pow]}).tail())

print("-----------------------------------------")


# 2-4. 나라별로 날짜의 최댓값과 최솟값의 차이 구하기
def get_diff_date(df: pd.core.fram.DataFram):
    # apply()로 전달하는 함수의 파라미터는 각 그룹의 DataFrame 타입 데이터읻.
    return df.df_date.max() - df.df_date.min()

by_contry.apply(get_diff_date)