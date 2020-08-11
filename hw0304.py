x = input()

if 'h' in x and 'e' in x and 'l' in x and 'o' in x:
    a = x.find('h')
    x = x[a+1:]
    if 'e' in x and 'l' in x and 'o' in x:
        b = x.find('e') 
        x = x[b+1:]
        if 'l' in x and 'o' in x:
            c = x.find('l') 
            x = x[c+1:]
            if 'l' in x and 'o' in x:
                d = x.find('l') 
                x = x[d+1:]
                if 'o' in x:
                    print ('YES')
                else:
                    print ('NO')
            else:
                print ('NO') 
        else:
            print ('NO')
    else:
        print ('NO')
else:
    print ('NO')