a = input()

if 'AB' in a and 'BA' in a:
    b = a.find('AB')
    c = a.find('BA')
    if b < c:
        a = a[(b+2):]
        if 'BA' in a:
            print('YES')
        else:
            print('NO')
    else:
        a = a[(c+2):]
        if 'AB' in a:
            print('YES')
        else:
            print('NO')
else:
    print('NO')