age = 0
a = 0
first = 0
second = 0
i = 0

while True:
    a = int(input())
    if a == -1:
        break
    else:
        age = a
        if i == 0:
            second = age
            first = age
        if i == 1:
            if age > first:
                second = first
                first = age
            else:
                second = age
        if i > 1:
            if age > first:
                second = first
                first = age
            if age < first and age > second:
                second = age
        i = i + 1
print (first, second)