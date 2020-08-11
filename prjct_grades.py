import csv

from statistics import mean     

import operator

#taskone
def calculate_averages(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        d = {}
        k = 0
        for row in reader:
            k += 1
            gradelist = row[1:]
            gradelist = [float(grade) for grade in gradelist]
            d[row[0]] = mean(gradelist)
    with open (output_file_name, 'w') as fout:
        q = 1
        for item in list(d.keys()):
            if q < k:
                fout.write('%s,%s' %(item, d[item]))
                fout.write('\n')
                q += 1
            elif q == k:
                fout.write('%s,%s' %(item, d[item]))
        fout.close()

#tasktwo
def calculate_sorted_averages(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        d = {}
        namelist = []
        k = 0
        for row in reader:
            k += 1
            namelist.append(row[0])
            gradelist = row[1:]
            gradelist = [float(grade) for grade in gradelist]
            d[row[0]] = mean(gradelist)  
        sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
        d = dict(sorted_by_value)
        namelist = list(d.keys())
    with open (output_file_name, 'w') as fout:
        q = 1
        for name in namelist:
            if q < k:
                fout.write('%s,%s' %(name, d[name]))
                fout.write('\n')
                q += 1
            elif q ==k:
                fout.write('%s,%s' %(name, d[name]))
        fout.close()

#taskthree           
def calculate_three_best(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        d = {}
        namelist = []
        k = 0
        for row in reader:
            k += 1
            namelist.append(row[0])
            gradelist = row[1:]
            gradelist = [float(grade) for grade in gradelist]
            d[row[0]] = mean(gradelist)  
        sorted_by_value = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        d = dict(sorted_by_value)

        namelist = list(d.keys())
    with open (output_file_name, 'w') as fout:
        for i in range(2):
            if i < 2:
                fout.write('%s,%s' %(namelist[i], d[namelist[i]]))
                fout.write('\n')
                i += 1
            if i ==2:
                fout.write('%s,%s' %(namelist[i], d[namelist[i]]))
        fout.close()

#taskfour           
def calculate_three_worst(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        meanlist = []
        for row in reader:
            gradelist = row[1:]
            gradelist = [float(grade) for grade in gradelist]
            meanlist.append(mean(gradelist))
        meanlist.sort()
    with open (output_file_name, 'w') as fout:
        for i in range(2):
            if i < 2:
                fout.write('%s' %(meanlist[i]))
                fout.write('\n')
                i += 1
            if i == 2:
                fout.write('%s' %(meanlist[i]))
        fout.close()

#taskfive      
def calculate_average_of_averages(input_file_name, output_file_name):
    with open (input_file_name, 'r') as fin:
        reader = csv.reader(fin)
        meanlist = []
        for row in reader:
            gradelist = row[1:]
            gradelist = [float(grade) for grade in gradelist]
            meanlist.append(mean(gradelist))
    with open (output_file_name, 'w') as fout:
        fout.write( '%s' %(mean(meanlist)) )
        fout.close()

#calculate_averages ('grades.csv', 'taskone.csv')
#calculate_sorted_averages ('grades.csv', 'tasktwo.csv')
#calculate_three_best ('grades.csv', 'taskthree.csv')
calculate_three_worst ('grades.csv', 'taskfour.csv')
calculate_average_of_averages ('grades.csv', 'taskfive.csv')