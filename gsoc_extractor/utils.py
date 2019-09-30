import os
from fuzzywuzzy import fuzz

# algorithm to answer the raised query

def check(year):
    flag=0
    dataList = []
    test = 0
    files = os.listdir('Data/')
    with open("Data/ExtractedData.txt") as d:
        for l in d:
                dataList.append(l[0:len(l)-1])
    if year not in dataList:
        for filename in files:
            if(filename == "GSOC_"+year+"_Data.ods"):
                    test = 1
        if(test == 1):
            # print "Data of year " + year + " has not been extracted completely"
            os.system("rm "+"Data/GSOC_"+year+"_Data.ods")
        # else:
                # print "No Data of year " + year
        # print "Please run gsoc_yearly_data_generator.py for year " + year
        flag = 1
    return flag

def query(qtype, query):
    answer = []
    qtype = qtype.split(' ')
    if(qtype[0] == "gt"):
        if not check(qtype[1]):
            file_name = "GSOC_"+qtype[1]+"_Data.ods"	
            # input = raw_input("Technology name: ")
            with open("Data/"+file_name) as file:
                for line in file:
                    a = line.split(",")
                    a[len(a)-1] = a[len(a)-1][0:len(a[len(a)-1])-1]
                    for i in range(2,len(a)):
                        if(fuzz.partial_ratio(a[i],query    ) > 85):
                            answeri={}
                            answeri["Organization"] = a[0]
                            answeri["Technologies"] = a[2:len(a)]
                            answeri["link"] = a[1]
                            answer.append(answeri)
                            # print "Organization:  " + a[0]
                            # print "Technologies: ",
                            # print a[2:len(a)]
                            # print "Link:          " + a[1] + "\n"
                            break

    elif(qtype[0] == "co"):
        yearList = query.split(",")
        flag = 0
        for i in yearList: 
            if check(i): flag=1
        dicts = []
        for i in yearList: dicts.append({})
        count =0
        if(flag != 1):
            for i in yearList:
                file_name = "GSOC_"+i+"_Data.ods"
                with open("Data/"+file_name) as file:
                    for line in file:
                        line = line.split(",")
                        dicts[count][line[0]] = line[1:len(line)]
                count+=1
            commonL=[]
            for i in dicts[0].keys():
                tes=0
                for j in dicts:
                    if i not in j.keys():
                        tes=1
                if(tes==0): commonL.append([i,dicts[0][i]])


            for i in commonL:
                i[1][len(i[1])-1] = i[1][len(i[1])-1][0:len(i[1][len(i[1])-1])-1]
                answeri={}
                answeri["Organization"] = i[0]
                answeri["Technologies"] = i[1][1:len(i[1])]
                answeri["link"] = i[1][0]
                answer.append(answeri)
                # print "Organization:  " + i[0]
                # print "Technologies: ",
                # print i[1][1:len(i[1])]
                # print "Link:          " + i[1][0] + "\n"

    return answer