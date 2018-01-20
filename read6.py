# code for reading users csv file and then creating dictionary to get corresponding unique ids

import csv

print ('creating users dictionary')
users = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique = 0

for line in reader:

    print line
    print line[0]
    users[line[0]] = unique
    unique = unique + 1
print unique
print ('printing users dictionary...')
print users
print users['shaifu']