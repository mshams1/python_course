list = [] 
listLen = 10
for i in range(listLen):  
    list.append(input()) 
i = 0
for i in range(listLen):
    a = list[i]
    a = a.lower()
    b = a[0]
    b = b.upper()
    c = b[0] + a[1:]
    list[i] = c
    i = i + 1
i = 0
for i in range(listLen):
    print(list[i]) 
    i = i + 1