# code for adding coma in json file to bring it in correct format and then loading it
# final code
import json
from pprint import pprint

# print ('writing')
#
# with open("/home/diksha/IIITD/sem4/capstone/final files/ratings_new.json", 'w') as file:
#     with open("/home/diksha/IIITD/sem4/capstone/final files/ratings.json") as my_file:
#         for line in my_file:
#             line = ","+line
#             file.write(line)
#
#
# file.close()
#


json_data = open('/home/diksha/IIITD/sem4/capstone/final files/ratings_new.json')
data = json.load(json_data)
#print data
pprint(data)