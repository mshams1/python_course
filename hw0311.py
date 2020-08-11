n = int(input())

d = {}

for i in range (n):
    name = input()
    if name in list(d.keys()):
        d[name] = d[name] + 1
    else:
        d[name] = 1

b = list(d.keys())

b.sort()

#print (b)

for name in b:
    print ('%s %s' %(name, d[name]))