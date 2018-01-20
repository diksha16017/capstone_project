# code for reading json file simply line by line

import os

with open("/home/diksha/IIITD/sem4/capstone/ratings_1.json") as my_file:
    for line in my_file:
        print line


