listdata1 = ['a', 'b', 'c', 'd', 'e']
listdata2 = ['f', 'g', 'h', 'i', 'j']
listdata3 = listdata1 + listdata2
listdata4 = listdata2 + listdata1
print(listdata3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(listdata4)  # ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']
