a = input()

a = a.lower()

b = len(a)

c = b/2

d = int(c)

e = 0

for i in range(d):
    if a[i] != a[-i-1]:
        e = e + 1
        i = i + 1
if e == 0:
    print('palindrome')
else:
    print('not palindrome')