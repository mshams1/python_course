a = input()

a = [int(i) for i in a.split(' ')]

a.sort()

b = a[2] - a[0]

import math

b = math.floor (b)

b = int(b)

print (b)