names = {'Marry': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}
ks = names.keys()
print(ks)
# 사전은 순서가 없는 자료형이므로 dict_keys 객체 요소들의 순서는 매번 다름
# dict_keys(['Marry', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly'])


for k in ks:
    print('Key:%s \t Value:%d' % (k, names[k]))
# Key:Marry 	 Value:10999
# Key:Sams 	 Value:2111
# Key:Aimy 	 Value:9778
# Key:Tom 	 Value:20245
# Key:Michale 	 Value:27115
# Key:Bob 	 Value:5887
# Key:Kelly 	 Value:7855

keys_list = list(names.keys())
