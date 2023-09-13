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
