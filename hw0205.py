x = 1
c = 0
maxofn = 0
champion = 0
i = 0

def nofdivisorsfora(a, x, c):
    while x <= a:
        if a % x == 0:
            c = c + 1
        x = x + 1
    return c

for i in range(20):
    a = int(input())
    n = nofdivisorsfora(a, x, c)   
    if n == maxofn and a > champion:
        maxofn = n
        champion = a
    elif n > maxofn:
        maxofn = n
        champion = a
    i = i + 1

print (champion, maxofn)
