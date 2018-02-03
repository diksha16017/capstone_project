# code to load dictionary from text file
import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

with open("movie_dictionary") as tweetfile:
    pyresponse = json.load(tweetfile)


for key in pyresponse:
    print key,pyresponse[key]