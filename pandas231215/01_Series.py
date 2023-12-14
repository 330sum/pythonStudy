import pandas as pd

# Serise
temp = pd.Series([-20, 10, 10, 20])
print(temp)
print(temp[0])

# Serise 객체 생성 (인덱스 지정)
temp = pd.Series([-20, 10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
print(temp['Mar'])
print(temp['Dec'])
