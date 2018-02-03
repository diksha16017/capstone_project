import csv
import os
import json
from datetime import date

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

file = open("/home/diksha/IIITD/sem4/capstone/final files/final_files/users.csv", "r")
reader = csv.reader(file)

with open("user_dictionary") as tweetfile:
    user_dictionary = json.load(tweetfile)

i = 0

def findAge(born):

    day = int(born.split('-')[0])
    month = int(born.split('-')[1])
    year = int(born.split('-')[2])
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

with open("/home/diksha/IIITD/sem4/capstone/final files/final_files/map_user_age", 'w') as myfile:
    for line in reader:

        if i != 0:
            userName = line[0]
            corresponding_user_id = user_dictionary[userName]
            dob = line[4]
            age = findAge(dob)
            lines = str(corresponding_user_id) + "  " + str(age) + "\n"
            myfile.write(lines)

        i = i + 1

myfile.close()
