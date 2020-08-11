age = 0
a = 0
max = 0
while True:
    a = int(input())
    if a == -1:
        break    
    else:
        a = age
        if age >= max:
            max = age
print (max)