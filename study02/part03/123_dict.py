solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solardict = {}
for entry in enumerate(solar1):
    print(entry)  # 튜플

for i, k in enumerate(solar1):
    print(i, k)  # 인자풀기 -> 인덱스 0부터 시작

for i, k in enumerate(solar1, start=1):
    print(i, k)  # 인덱스 1부터 시작

for i, k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val

print(solardict)
# {'태양': 'Sun', '수성': 'Mercury', '금성': 'Venus', '지구': 'Earth', '화성': 'Mars', '목성': 'Jupiter', '토성': 'Saturn', '천왕성': 'Uranus', '해왕성': 'Neptune'}
