#find unique user ages

import os
import csv
import json
from datetime import date

print ('creating users unique age dictionary')
users_unique_age = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique = 1
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
i=0


def findAge(born):

    day = int(born.split('-')[0])
    month = int(born.split('-')[1])
    year = int(born.split('-')[2])
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age



for line in reader:

    if i != 0:
        dob = line[4]
        print dob
        age = findAge(dob)
        users_unique_age[age] = unique
        unique = unique + 1
    i = i + 1


print 'users unique age'
print users_unique_age

with open("/home/diksha/IIITD/sem4/capstone/final files/user_age_list", 'w') as myfile:
    myfile.write(json.dumps(users_unique_age))
myfile.close()

print len(users_unique_age)
