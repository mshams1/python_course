import random

lowerbound = 1
higherbound = 99

newguess = random.randint(lowerbound,higherbound)

print(newguess)

nazar = input()

while True:
    lastguess = newguess  
    if nazar == 'k':
        higherbound = lastguess
        newguess = random.randint(lowerbound, higherbound)
        print (newguess)
        nazar = input()
    elif nazar == 'b':
        lowerbound = lastguess
        newguess = random.randint(lowerbound, higherbound)
        print (newguess)
        nazar = input()
    elif nazar == 'd':
        print ('well done')
        break
    elif nazar == 'finish':
        print ('bye')
        break
    elif nazar != 'b' or 'k' or 'd' or 'finish':
        print ('wrong input! give b, k or d or finish if you are done:')
        nazar = input()
