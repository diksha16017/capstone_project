# code for adding coma in json file to bring it in correct format and then loading it

import json
from pprint import pprint

json_data = open('/home/diksha/IIITD/sem4/capstone/ratings_1.json')
data = json.load(json_data)
#print data
pprint(data)
# print ('writing')
#
# with open("/home/diksha/IIITD/sem4/capstone/ratings_1_1.json", 'w') as file:
#     with open("/home/diksha/IIITD/sem4/capstone/rating.json") as my_file:
#         for line in my_file:
#             line = ","+line
#             file.write(line)
#
#
# file.close()
#
#


#data = json.load(open('ratings_1.json'))
#pprint(data)

#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]







