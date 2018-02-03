import csv
import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

file = open("/home/diksha/IIITD/sem4/capstone/final files/final_files/movies_1.csv", "r")
reader = csv.reader(file)

with open("movie_dictionary") as tweetfile:
    user_dictionary = json.load(tweetfile)

i = 0

with open("/home/diksha/IIITD/sem4/capstone/final files/final_files/map_movie_language", 'w') as myfile:
    for line in reader:

        if i != 0:
            userName = line[0]
            corresponding_user_id = user_dictionary[userName]
            line[1] = line[1].translate(None, ' []"') #remove double quotes, [] and extra space also
            check = line[1].split(",")
            for k in check:
                lines = str(corresponding_user_id) + "  " + k + "\n"
                myfile.write(lines)

        i = i + 1

myfile.close()
