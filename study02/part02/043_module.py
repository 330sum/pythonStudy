import time

print('5초간 프로그램 정지함')
time.sleep(5)
print('5초 지남')

import mylib
ret1= mylib.add_txt('밤비', '1등')
ret2 = mylib.reverse(1,2,3)
print(ret1)
print(ret2)
