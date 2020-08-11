b = input()

a = input()

a = [int(i) for i in a.split(' ')]

c =  0

for i in a:
    if i < 3:
        c = c+1

d = c/3

from math import floor

d = floor (d)

d = int(d)

print (d)