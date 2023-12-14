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

print(df['키'] >= 185)  # True, False 로 나옴
filt = df['키'] >= 185
print(df[filt])
print(df[~filt])
print(df[df['키'] >= 185])
print(df.loc[df['키'] >= 185, '수학'])
print(df.loc[df['키'] >= 185, ['이름', '수학', '영어']])
print(df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')])
print(df.loc[(df['키'] < 170) | (df['키'] > 200)])

# str 함수
filt = df['이름'].str.startswith('송')
print(df[filt])
filt = df['이름'].str.contains('태')
print(df[filt])
print(df[~filt])

langs = ['Python', 'Java']
filt = df['SW특기'].isin(langs)
print(df[filt])

langs = ['python', 'java']
filt = df['SW특기'].str.lower().isin(langs)
print(df[filt])

filt = df['SW특기'].str.contains('Java')
print(df[filt])
