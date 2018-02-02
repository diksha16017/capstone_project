# code for reading users csv file and then creating dictionary to get corresponding unique ids
# use read6 and read7
import csv

print ('creating users dictionary')
users = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique = 0

i = 1
for line in reader:

    if i == 11:
        print line
        for k in line:
            print k
        line[1] = line[1].translate(None, ' []"') #remove double quotes, [] and extra space also
        #line[1] = line[1].replace("[", "")
        #line[1] = line[1].replace("]","")
        print line[1]
        check = line[1].split(",")
        for k in check:
            print k
    users[line[0]] = unique
    unique = unique + 1
    i = i + 1
#print unique
#print ('printing users dictionary...')
#print users
#print users['shaifu']