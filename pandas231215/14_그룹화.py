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

print(df.groupby('학교'))  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x104f3f1d0>
print(df.groupby('학교').get_group('북산고'))
print(df.groupby('학교').get_group('능남고'))

# print(df.groupby('학교').mean()) # 계산 가능한 데이터들의 평균값
print(df.groupby('학교').size())  # 각 그룹의 크기
print(df.groupby('학교').size()['능남고'])  # 학교로 그룹화한 뒤에 능남고에 해당하는 데이터의 수
print(df.groupby('학교')['키'].mean())  # 학교로 그룹화한 뒤, 키의 평균 데이터
print(df.groupby('학교')[['국어', '영어', '수학']].mean())  # 학교로 그룹화한 뒤, 국영수의 평균 데이터

df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]  # 학년 컬럼 추가
print(df)

# print(df.groupby(['학교', '학년']).mean())  # 학교별, 학년별 평균 데이터
# print(df.groupby('학년').mean())  # 학년별 평균 데이터
# print(df.groupby('학년').mean().sort_values('키'))
# print(df.groupby('학년').mean().sort_values('키', ascending=False))
print(df.groupby('학교')['SW특기'].count())  # 학교로 그룹화 한 후, 학교별 SW특기 데이터 수 가져오기
print(df.groupby('학교')[['이름', 'SW특기']].count())

print('============================================')
# 학교를 그룹화 한 뒤, 학년 별 학생 수 가져오기
school = df.groupby('학교')
print(school['학년'].value_counts())

# 학교를 그룹화 한 뒤, 북산고에서 학년별로 학생 수 가져오기
print(school['학년'].value_counts().loc['북산고'])

# 학교를 그룹화 한 뒤, 능남고에서 학년별로 학생 수 가져오기
print(school['학년'].value_counts().loc['능남고'])

# 학생들의 수 데이터를 퍼센트로 비교하여 가지고 옴
print(school['학년'].value_counts(normalize=True).loc['북산고'])
