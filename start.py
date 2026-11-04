
 # generate random between 0 and 100

import random

x = random.randint(0, 100)

print(x)


result = x

if result % 2 == 0:
    print("even")
else:
    print("odd")