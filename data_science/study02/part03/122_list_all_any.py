listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))  # False - 0 때문에
print(any(listdata1))  # True
print(all(listdata2))  # True
print(any(listdata2))  # True
print(all(listdata3))  # False
print(any(listdata3))  # False

# all() 모든 요소가 참인 경우, True
# any() 모든 요소가 거짓인 경우, False
