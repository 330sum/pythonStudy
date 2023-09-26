solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solarsys))
print(ret)
# [(0, '태양'), (1, '수성'), (2, '금성'), (3, '지구'), (4, '화성'), (5, '목성'), (6, '토성'), (7, '천왕성'), (8, '해왕성')]

for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체: %s' % (i, body))


# ======================================================
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i, val in enumerate(a):
    print(i, val, a[i])

