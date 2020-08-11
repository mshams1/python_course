n = int(input())

d = {}

for i in range (n):
    a = input().split(' ')
    d [a[0]] = a[1]

phrase = input().split(' ')

a = []

for word in phrase:
    if word in list(d.keys()):
        a.append(d[word])
    else:
        a.append(word)
print (' '.join(a))