# code for reading json file for finding unique user-id and movies rated by that particular user

import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files")
json_data = open('ratings_test1.json')
data = json.load(json_data)

number_ids_in_key = len(data["key"])
print number_ids_in_key

for i in range(number_ids_in_key):
    user_id = data["key"][i]["_id"]
    count = 0
    for d in data["key"][i]["rated"]:
        if d[0] == 't':
            count = count + 1
            print user_id, d, data["key"][i]["rated"][d][0]
    print count
    print "**********************************************************"
