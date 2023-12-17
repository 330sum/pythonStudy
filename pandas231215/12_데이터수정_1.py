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

# column 수정
df['학교'].replace({'북산고': '상북고', '능남고': '무슨고'}, inplace=True)
print(df)

df['SW특기'] = df['SW특기'].str.lower()
print(df)

df['학교'] = df['학교'] + '등학교'
print(df)

# column 추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

df['결과'] = 'Fail'  # 결과 컬럼 추가, Fail로 초기화
print(df)

# df.loc[row, column]
df.loc[df['총합'] > 400, '결과'] = 'Pass'  # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 변경
print(df)

# column 삭제
df.drop(columns=['총합'], inplace=True)
print(df)

df.drop(columns=['과학', '사회'], inplace=True)
print(df)

# row 삭제
df.drop(index=['8번'], inplace=True)
print(df)

filt = df['수학'] < 80
print(filt)
print(df[filt])
print(df[filt].index)  # Index(['2번', '3번', '4번', '5번', '7번'], dtype='object', name='지원번호')
df.drop(index=df[filt].index, inplace=True)
print(df)

# row 추가
df.loc['9번'] = ['박수민', '삼현고등학교', 165, 90, 90, 90, 'kotlin', 'Pass']
print(df)
