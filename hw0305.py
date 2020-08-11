a = input()

b = a.upper()
c = a.lower()

k = 0

for i in range(len(a)):
    if a[i] in b:
        k = k + 1
#print (k)
if k > (len(a)/2):
    print(b)
else:
    print(c)

