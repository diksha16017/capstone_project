import csv
import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

file = open("/home/diksha/IIITD/sem4/capstone/final files/final_files/users.csv", "r")
reader = csv.reader(file)

with open("user_dictionary") as tweetfile:
    user_dictionary = json.load(tweetfile)

i = 0

with open("/home/diksha/IIITD/sem4/capstone/final files/final_files/map_user_job", 'w') as myfile:
    for line in reader:

        if i != 0:
            userName = line[0]
            corresponding_user_id = user_dictionary[userName]
            lines = str(corresponding_user_id) + "  " + line[2] + "\n"
            myfile.write(lines)

        i = i + 1

myfile.close()
