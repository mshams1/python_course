n = int(input())

a = []

for i in range(n):
    num = int(input())  
    a.append(num)

from math import sqrt
from math import floor

for num in a:
    b = sqrt(num)
    c = floor(b*10**4)
    c = str(c)
    print (c[:-4] + '.' + c[-4:])
