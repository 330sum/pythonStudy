import pandas as pd
import numpy as np

data = {
    '이름': ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교': ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키': [197, 184, 168, 187, 188, 202, 188, 190],
    '국어': [90, 40, 80, 40, 15, 80, 55, 100],
    '영어': [85, 35, 75, 60, 20, 100, 65, 85],
    '수학': [100, 50, 70, 70, 10, 95, 45, 90],
    '과학': [95, 55, 80, 75, 35, 85, 40, 95],
    '사회': [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기': ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
df.index.name = '지원번호'
print(df)

# 빈 값을 NaN으로 변환
df.replace('', np.nan, inplace=True)
print(df)

# 전체 데이터 중에서 NaN을 포함하는 데이터 삭제
# axis: index or columns
#  NaN를 포함하는 index / columns 삭제
# how: any or all
#  NaN를 포함하는 index / columns 중에서 해당하는 것(any)만 삭제 / 전체가 Nan일때(all) 삭제

# df.dropna(axis='index', how='any', inplace=True)
# df.dropna(axis='columns', how='any', inplace=True)
# df.dropna(axis='index', how='all', inplace=True)

df['학교'] = np.nan
df.dropna(axis='columns', how='all', inplace=True)
# 학교 데이터의 모든 값이 NaN이니까 학교 컬럼 삭제
# SW특기 데이터는 일부만 NaN이니까 삭제 안됨
print(df)
