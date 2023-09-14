from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)
mylib.add_txt('hi', 'python')
reverse(1, 2, 3)

import mypackage

mypackage.mylib.add_txt('hi', 'python')
