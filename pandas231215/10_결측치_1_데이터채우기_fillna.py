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

# fillna 메서드는 기본적으로 DataFrame의 복사본을 반환하므로 원본 DataFrame이 수정되지 않습니다.
# 따라서 df.fillna('없음') 및 df.fillna('모름')의 결과를 출력하거나 새로운 변수에 할당하지 않으면 변경 사항이 반영되지 않습니다.

# 만약 원본 데이터를 바꾸고 싶으면 inplace=True 사용!
# df.fillna('없음', inplace=True)

# 데이터 채우기
df_filled = df.fillna('없음')
print(df_filled)

df['학교'] = np.nan  # 학교데이터를 NaN으로 변경
print(df)
df_filled_unknown = df.fillna('모름')
print(df_filled_unknown)
print(df.fillna('모름'))
