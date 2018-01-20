# code for parsing json file for creating user-item matrix

import os
import json
from pprint import pprint

os.chdir("/home/diksha/IIITD/sem4/capstone")
#data = json.load(open('ratings_1.json'))
#pprint(data)

#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]


json_data = open('ratings_1.json')
data = json.load(json_data)
pprint(data)
print(data["key"][0]["rated"])
len = len(data["key"][0]["rated"])
print (len)
for d in data["key"][0]["rated"]:
    print d
    print (data["key"][0]["rated"][d][0])

#pprint(data[0])
#pprint(data._id[1])

