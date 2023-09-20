names = {'Marry': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}
ret1 = sorted(names)
print(ret1)


# ['Aimy', 'Bob', 'Kelly', 'Marry', 'Michale', 'Sams', 'Tom']


def f1(x):
    return x[0]


def f2(x):
    return x[1]


ret2 = sorted(names.items(), key=f1)
print(ret2)
# [('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Marry', 10999), ('Michale', 27115), ('Sams', 2111), ('Tom', 20245)]

ret3 = sorted(names.items(), key=f2)
print(ret3)
# [('Sams', 2111), ('Bob', 5887), ('Kelly', 7855), ('Aimy', 9778), ('Marry', 10999), ('Tom', 20245), ('Michale', 27115)]

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)
# [('Michale', 27115), ('Tom', 20245), ('Marry', 10999), ('Aimy', 9778), ('Kelly', 7855), ('Bob', 5887), ('Sams', 2111)]
