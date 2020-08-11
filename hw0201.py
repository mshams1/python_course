a = int (input())
x = 1
c = 0
while x != a:
    if a%x == 0:
        c = c + 1
    x = x + 1

if c != 1:
    print ("not prime")
else:
    print ("prime")