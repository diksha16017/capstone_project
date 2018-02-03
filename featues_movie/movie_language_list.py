#finding unique languages of movie

import os
import csv
import json

print ('creating movies unique languages dictionary')
movie_unique_languages = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/final_files/movies_1.csv", "r")
reader = csv.reader(file)
unique = 1

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
i=0

for line in reader:

    if i != 0:

        line[1] = line[1].translate(None, ' []"')
        check = line[1].split(",")
        for k in check:
            #print k
            movie_unique_languages[k] = unique
            unique = unique + 1
    i = i + 1


print 'movie unique languages'
print len(movie_unique_languages)
#
# with open("/home/diksha/IIITD/sem4/capstone/final files/movie_language_list", 'w') as myfile:
#     myfile.write(json.dumps(movie_unique_languages))
# myfile.close()