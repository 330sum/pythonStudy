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

print(df.sort_values('키'))  # 키 기준으로 오름차순 정렬
print(df.sort_values('키', ascending=False))  # 키 기준으로 내림차순 정렬
print(df.sort_values(['수학', '영어']))
print(df.sort_values(['수학', '영어'], ascending=False))
print(df.sort_values(['수학', '영어'], ascending=[True, False]))  # 수학으로 오름차순한 다음, 같은 값이면 영어 내리차순으로
print(df['키'].sort_values())
print(df['키'].sort_values(ascending=False))
print(df.sort_index())
print(df.sort_index(ascending=False))
