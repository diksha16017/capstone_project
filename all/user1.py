#finding unique languages of user

import os
import csv
import json

print ('creating users unique languages dictionary')
users_unique_languages = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique = 1
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
i=0

for line in reader:

    if i != 0:
        #print line
        line[1] = line[1].translate(None, ' []"') #remove double quotes, [] and extra space also
        check = line[1].split(",")
        for k in check:
            users_unique_languages[k] = unique
            unique = unique + 1
    i = i + 1


print 'users unique languages'
print users_unique_languages

with open("/home/diksha/IIITD/sem4/capstone/final files/user_language_list", 'w') as myfile:
    myfile.write(json.dumps(users_unique_languages))
myfile.close()