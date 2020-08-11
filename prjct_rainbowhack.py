import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
      
        d = {}
        for i in range(0,10):
            i = str(i)
            arzesh = "000" + i
            kilid = hashlib.sha256(arzesh.encode('utf-8')).hexdigest()
            d[kilid] = arzesh
        for i in range(10,100):
            i = str(i)
            arzesh = "00" + i
            kilid = hashlib.sha256(arzesh.encode('utf-8')).hexdigest()
            d[kilid] = arzesh
        for i in range(100,1000):
            i = str(i)
            arzesh = "0" + i
            kilid = hashlib.sha256(arzesh.encode('utf-8')).hexdigest()
            d[kilid] = arzesh
        for i in range(1000,10000):
            arzesh = str(i)
            kilid = hashlib.sha256(arzesh.encode('utf-8')).hexdigest()
            d[kilid] = arzesh

        dd = {}
        hashresultlist = []
        k = 0
        for row in reader:
            k += 1
            hashname = row[0]
            hashresult = row[1]
            dd [hashresult] = hashname
            hashresultlist.append(hashresult)

    with open (output_file_name, 'w') as fout:
        q = 1
        for item in hashresultlist:
            if item in list(d.keys()) and q < k:
                fout.write('%s,%s' %(dd[item], d[item]))
                fout.write('\n')        
                q += 1        
            elif item in list(d.keys()) and q == k:
                fout.write('%s,%s' %(dd[item], d[item]))
        fout.close()

