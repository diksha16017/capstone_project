import csv
import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files")

movies = dict()
users = dict()

print ('creating users dictionary')
file = open("/home/diksha/IIITD/sem4/capstone/final files/users.csv", "r")
reader = csv.reader(file)
unique_user = 0
for line in reader:
    users[line[0]] = unique_user
    unique_user = unique_user + 1
print ('users dictionary over....')

print ('*****************************************')

print ('creating movies dictionary')
file = open("/home/diksha/IIITD/sem4/capstone/final files/movies.csv", "r")
reader = csv.reader(file)
unique_movie = 0
for line in reader:
    movies[line[0]] = unique_movie
    unique_movie = unique_movie + 1
print ('movies dictionary over...')

print ('*****************************************')

json_data = open('ratings_new.json')
data = json.load(json_data)

number_ids_in_key = len(data["key"])
print "number of unique user IDs",number_ids_in_key

with open("/home/diksha/IIITD/sem4/capstone/final files/final_ratings", 'w') as myfile:
    for i in range(number_ids_in_key):
        user_id = users[data["key"][i]["_id"]]
        count = 0
        for d in data["key"][i]["rated"]:
            if d[0] == 't':
                count = count + 1
                lines = str(user_id) + "  " + str(movies[d]) + "  " + str(data["key"][i]["rated"][d][0])+"\n"
                myfile.write(lines)

        print count
        print "**********************************************************"
myfile.close()

with open("/home/diksha/IIITD/sem4/capstone/final files/user_dictionary", 'w') as myfile:
    myfile.write(json.dumps(users))
myfile.close()

with open("/home/diksha/IIITD/sem4/capstone/final files/movie_dictionary", 'w') as myfile:
    myfile.write(json.dumps(movies))
myfile.close()