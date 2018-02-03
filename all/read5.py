# code for reading a CSV file

import csv

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
i = 0
for line in reader:
    if i == 3:
        break
    print line
    print line[0]
    i = i + 1