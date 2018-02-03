# code for finding data corresponding to user id and corresponding movie id and rating from the json file

import os
import json
from pprint import pprint

os.chdir("/home/diksha/IIITD/sem4/capstone/final files")

json_data = open('ratings_test1.json')
data = json.load(json_data)

pprint(data)
lenn = len(data["key"])
print lenn
user_id = data["key"][0]["_id"]

#print (data["key"][0]["_id"])
#print(data["key"][0]["rated"])
#len = len(data["key"][0]["rated"])
#print (len)

count  = 0
for d in data["key"][0]["rated"]:
    #print d
    #print (data["key"][0]["rated"][d][0])
    if d[0] == 't':
        count = count + 1
        print user_id,d,data["key"][0]["rated"][d][0]

print count
#pprint(data[0])
#pprint(data._id[1])

