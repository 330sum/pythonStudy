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
print(df)
print(df.index)  # Index(['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'], dtype='object')
print()

# 인덱스 이름 설정
df.index.name = '지원번호'
print(df)
print()

# 인덱스 삭제
index = df.reset_index()  # 컬럼으로 들어옴
print(index)
print()

reset_index = df.reset_index(drop=True)  # 진짜 인덱스 삭제하는데, 인덱스가 초기화됨 0,1,2..
print(reset_index)
print(df)  # 인덱스를 삭제하고 했는데, 원본은 그대로임
print()

df.reset_index(drop=True, inplace=True)  # inplace=True 실제 데이터에 바로 반영 (변수로 뺄 수 없음. 원본은 1개이기 때문에)
print(df)

set_index = df.set_index('이름')  # 이름이 인덱스가 됨
print(set_index)

df.set_index('이름', inplace=True)
print(df)

# 인덱스 정렬
sort_index = df.sort_index()  # 오름차순
print(sort_index)

df_sort_index = df.sort_index(ascending=False)  # 내림차순
print(df_sort_index)
