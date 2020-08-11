a = input ()
i = 0 
while i < len(a): 
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' or a[i] == 'A' or a[i] == 'E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U':
        a = a[0:i] + a[i+1: len(a)]
        i = i
    else:
        i = i  + 1
a = a.lower()
i = 0
while i < len(a):
    a = a[0:i] +'.'+ a[i: len(a)]    
    i = i + 2
print(a)