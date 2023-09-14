# 22개의 행과 4개의 열을 갖는 딕셔너리를 정의
import pandas as pd

heroes = {
    "name": [
        'ana', 'bastion', 'dva',
        'genji', 'hanjo', 'junkrat',
        'lucio', 'macree', 'mei',
        'mercy', 'pharah', 'reaper',
        'reinhardt', 'roadhog', 'soldier76',
        'symmetra', 'torbjorn', 'tracer',
        'widowmaker', 'winston', 'zarya',
        'zenyatta'
    ],
    "health": [
        200, 300, 500,
        200, 200, 200,
        200, 200, 250,
        200, 200, 250,
        500, 600, 200,
        200, 200, 150,
        200, 500, 400,
        200
    ],
    "position": [
        "support", "defense", "tank",
        "offense", "defense", "defense",
        "support", "offense", "defense",
        "support", "offense", "offense",
        "tank", "tank", "offense",
        "support", "defense", "offense",
        "defense", "tank", "tank",
        "support"
    ],
    "id": [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        10, 11, 12,
        13, 14, 15,
        16, 17, 18,
        19, 20, 21,
        22
    ]
}

heroes_df = pd.DataFrame(heroes)
print(heroes_df)

heroes_df.to_csv("/Users/superstar_park/PycharmProjects/heroes.csv")

heroes_df.to_excel("/Users/superstar_park/PycharmProjects/heroes.xlsx")
# heroes_df.to_excel("/Users/superstar_park/PycharmProjects/heroes.xlsx", index=False)
# index=False 설정하면 인덱스 저장하지 않을 수 있음

# 여러가지 형태로 데이터 다루기
print("========================================")
# 열 이름 -> 데이터
print(heroes_df[["name", "position"]])

# 불리언 인덱싱
print("========================================")
# 기본
print(heroes_df[heroes_df.health == 250])

print("========================================")
# 불리언 인덱싱의 조건 코드 실행
print(heroes_df.health == 250)

print("========================================")
# 두 가지 조건을 결합해 불리언 인덱싱 실행
print(heroes_df[(heroes_df.position == "tank") & (heroes_df.health > 500)])

print("========================================")
# #인덱스 기준에 따라 데이터 다루기
# 인덱스를 id라는 열로 변경하기
heroes_df.set_index('id', inplace=True)
print(heroes_df.head())

print("========================================")
# loc()
# id값이 3인 행 값을 모두 선택해서 가져옴
print(heroes_df.loc[3])

print("========================================")
# iloc()
# 인덱스가 3인 행 값을 모두 선택해서 가져옴
print(heroes_df.iloc[3])

print("==========================================")
# 1-6. 여러 개 인덱스로 그룹화하기
# postion 열로 먼저 그룹화하고, 그 안에서 health 열을 한 번 더 그룹화한다
multi_indexed = heroes_df.groupby(['position', 'health'])

# 앞 groupby로 그룹화된 데이터를 설명하는 내용을 출력
# 각 그룹 안의 전체 정보 (개수, 유일한 값의 개수, 최댓값을 가진 인덱스, 출현 빈도)를 보여줌
print(multi_indexed.describe())
