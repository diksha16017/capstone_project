#finding unique jobs of user
#finding unique states of user

import os
import csv
import json

print ('creating users unique languages dictionary')
users_unique_states = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique = 1
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
i=0

for line in reader:

    if i != 0:
        users_unique_states[line[3]] = unique
        unique = unique + 1
    i = i + 1


print 'users unique states'
print users_unique_states

with open("/home/diksha/IIITD/sem4/capstone/final files/user_state_list", 'w') as myfile:
    myfile.write(json.dumps(users_unique_states))
myfile.close()