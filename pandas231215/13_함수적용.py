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


def add_cm(height):
    return str(height) + 'cm'


df['키'] = df['키'].apply(add_cm)
print(df)


def capitalize(lang):
    if pd.notnull(lang):  # NaN이 아닌지 확인
        return lang.capitalize()  # 첫글자는 대문자, 나머지는 소문자
    return lang


# df['SW특기'] = df['SW특기'].apply(capitalize)
# print(df)
# 위 함수를 굳이 만들 필요 없이, str에 같은 거 있음
df['SW특기'] = df['SW특기'].str.capitalize()
print(df)
