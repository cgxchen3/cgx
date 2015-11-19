import re

rule1 = re.compile(r'.* Populate Started')
rule2 = re.compile(r'.*Running the backend components')
rule3 = re.compile(r'.*Aggregating...')
rule4 = re.compile(r'.*Running Post Processor.*')
rule5 = re.compile(r'.*Running Post Processor.*')
rule6 = re.compile(r'.*No tables require profiling')
array = [0] * 10
i = 0

f = open(r"C:\Users\cgx\Desktop\For Andy\TOM_TomLog.txt")
while True:  
    line = f.readline()  
    if line:
        if re.match(rule1,line):
            time = line.split(' ')
            time = time[0].split(':')
            time1 = [time[0],time[1],time[2]]
        if re.match(rule2,line):
            time = line.split(' ')
            time = time[0].split(':')
            time2 = [time[0],time[1],time[2]]
            print('prepare time:')
            for i in range(0,3):
                print(int(time2[i]) - int(time1[i]))
        if re.match(rule3,line):
            time = line.split(' ')
            time = time[0].split(':')
            time3 = [time[0],time[1],time[2]]
        if re.match(rule4,line):
            time = line.split(' ')
            time = time[0].split(':')
            time4 = [time[0],time[1],time[2]]
            print('aggregating time:')
            for i in range(0,3):
                print(int(time4[i]) - int(time3[i]))
        if re.match(rule5,line):
            time = line.split(' ')
            time = time[0].split(':')
            time5 = [time[0],time[1],time[2]]
        if re.match(rule6,line):
            time = line.split(' ')
            time = time[0].split(':')
            time6 = [time[0],time[1],time[2]]
            print('table_build time:')
            for i in range(0,3):
                print(int(time6[i]) - int(time5[i]))
f.close() 
