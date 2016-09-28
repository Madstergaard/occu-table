import csv
import random

dic = {}
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (row[0] != "Job Class" and row[0] != "Total"):
            dic[row[0]] = row[1]

def retD():
	return dic 

def jobme():
    counter = 0
    choose = random.uniform(0,99.8)
    for i in dic:
        counter += dic[i]
        if choose <= counter:
            return i
       
