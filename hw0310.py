n = int(input())

a = []

for i in range(n):
    b = input()
    b = b.split(' ')
    b = [int(i) for i in b]
    a.append(b)

c = []

for x in range(0, n-2):
    for y in range(1,n-x):
        if (a[x][0] - a[x+y][0]) == 0 and (a[x][1] - a[x+y][1]) == 0:
            d = 1
        else:
            d = ((a[x][0] - a[x+y][0])*(a[x][1] - a[x+y][1]))
        c.append(d)

if (a[n-2][0] - a[n-1][0]) == 0 and (a[n-2][1] - a[n-1][1]) == 0:
    e = 1
else:
    e = ((a[n-2][0] - a[n-1][0])*(a[n-2][1] - a[n-1][1]))

#print (e)

c.append(e)

#print (c)

r = 0

for i in c:
    if i <= 0:
        r = r + 1

#print (r)

if r == 0:
    print('poor irsa')
else:
    print('happy irsa')