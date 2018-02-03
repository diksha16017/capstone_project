import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

with open("users_features_dictionary") as userfile:
    user_features = json.load(userfile)


with open("movie_features_dictionary") as moviefile:
    movie_features = json.load(moviefile)

print len(user_features)
print len(movie_features)
print user_features['1']
print movie_features['1']

x = []
x.append(user_features[str(1)] + movie_features[str(1)])
x.append(user_features[str(2)] + movie_features[str(2)])
print x
print len(x)
