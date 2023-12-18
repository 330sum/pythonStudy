import pandas as pd

# 배점 기준
data1 = {
    '센터코드': ['LA', 'LA', 'LA', 'KS', 'KS', 'KS', 'OTC', 'OTC', 'OTC'],
    '평가': ['상', '중', '하', '상', '중', '하', '상', '중', '하'],
    '점수': ['10', '9', '8', '7', '6', '5', '4', '3', '2']
}

df1 = pd.DataFrame(data1)

# 결과 테이블
data2 = {
    '센터코드': ['LA', 'KS', 'KS', 'OTC', 'OTC', 'OTC'],
    '이름': ['AA', 'BB', 'CC', 'DD', 'EE', 'FF'],
    '평가': ['상', '중', '하', '상', '중', '하']
}

df2 = pd.DataFrame(data2)

# 결과를 저장할 빈 리스트
result_scores = []

# df2를 기반으로 df1에 평가에 따른 점수 추가
for index, row in df2.iterrows():
    center_code = row['센터코드']
    evaluation = row['평가']

    # 조건에 맞는 점수 찾기
    score = df1[(df1['센터코드'] == center_code) & (df1['평가'] == evaluation)]['점수'].values[0]

    # 결과 리스트에 추가
    result_scores.append(score)

# 결과 테이블에 새로운 컬럼으로 추가
df2['점수'] = result_scores

# 최종 결과 출력
print(df2)
print(df2.iloc[1]['이름'])
print(df2['이름'][1])