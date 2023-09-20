names = {'Marry': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}
vals = names.values()
print(vals)
# dict_values([10999, 2111, 9778, 20245, 27115, 5887, 7855])

vals_list = list(vals)
ret = sum(vals_list)
print('출생아 수 총계: %d' % ret)
# 출생아 수 총계: 83990
