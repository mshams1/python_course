i = 0
gp = 0
tp = 0
tw = 0
for i in range(30):
    gp = int(input())
    if gp == 3:
        tw = tw + 1
    tp = tp + gp
    i = i + 1
print (tp, tw)