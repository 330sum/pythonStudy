def reverse(x, y, z):
    return z, y, x


ret = reverse(1, 2, 3)
print(ret)  # [출력] (3, 2, 1)

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3) # [출력] c, b, a
