# code for reading movies csv file and then creating dictionary to get corresponding unique ids

import csv

print ('creating movies dictionary')
movies = dict()

file = open("/home/diksha/IIITD/sem4/capstone/final files/movies.csv", "r")
reader = csv.reader(file)
unique = 0

for line in reader:

    print line
    print line[0]
    movies[line[0]] = unique
    unique = unique + 1

print unique
print ('printing movies dictionary...')
print movies

#print movies['tt0231455']
print len(movies)