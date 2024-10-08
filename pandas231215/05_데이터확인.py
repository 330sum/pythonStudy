import pandas as pd

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
print(df.describe())  # 계산가능한 데이터에 대해 컬럼별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌
print(df.info())  # 데이터 정보
print(df.head())  #
print(df.head(7))
print(df.tail())  # 마지막 5개
print(df.tail(3))
print(df.values)
print(df.index)
print(df.columns)
print(df.shape)  # (8, 9) (row, column)

# Series 확인
print(df['키'].describe())
print(df['키'].max())
print(df['키'].min())
print(df['키'].nlargest(3))  # 키 큰 사람 순서대로 3사람
print(df['키'].mean())
print(df['키'].sum())
print(df['SW특기'].count())  # 8... 6.... 뭐지..? (현재는 8로 나옴)
print(df['학교'].unique())
print(df['학교'].nunique())
