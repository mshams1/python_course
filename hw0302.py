a = input ()

x = 0
y = 0
z = 0

for letter in a: 
    if letter == '1':
        x = x + 1
    if letter == '2':
        y = y + 1 
    if letter == '3':
        z = z + 1
a = '1' * x + '2' * y + '3' * z
i = 1
while i < len(a):
    a = a[0:i] +'+'+ a[i: len(a)]    
    i = i + 2
print (a)