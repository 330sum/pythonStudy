import pandas as pd
import numpy as np

s = pd.Series(
    ["s", "u", "m", 3, 30, 93.3], index=["A", "B", "C", "a", "b", "c"]
)

print(s)

heroes_dict = {
    'ana': 200, 'bastion': 300, 'dva': 500,
    'genji': 200, 'hanjo': 200, 'junkrat': 200,
    'lucio': 200, 'macree': 200, 'mei': 250,
    'mercy': 200, 'pharah': 200, 'reaper': 250,
    'reinhardt': 500, 'roadhog': 600, 'soldier76': 200,
    'symmetra': 200, 'torbjorn': 200, 'tracer': 150,
    'widowmaker': 200, 'winston': 500, 'zarya': 400,
    'zenyatta': 200
}

heroes_series = pd.Series(heroes_dict)
print(heroes_series)

# 여러가지 형태로 데이터 다루기
print("========================================")
# 인덱스(숫자) -> 데이터
print(heroes_series[0])

# 인덱스 슬라이스 -> 인덱스-데이터
print((heroes_series[3:7]))  # 3~6 가져오기

# 인덱스(문자열) -> 데이터
print(heroes_series['dva'])

# 불리언 인덱싱
print("========================================")
# 기본
print(heroes_series[heroes_series >= 250])
