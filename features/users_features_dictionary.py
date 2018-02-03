import os
import json
import csv

user_features = dict()
user_features_1 = dict()
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

# 0-7 age

features = {
        'Male': 8,
        'Female': 9,
        'Retired': 10,
        'Service': 11,
        'Self-employed': 12,
        'Student': 13,
        'Others': 14,
        'Haryanvi': 15,
        'Bengali': 16,
        'Oriya': 17,
        'Assamese': 18,
        'Punjabi': 19,
        'Marathi': 20,
        'Tamil': 21,
        'Gujarati': 22,
        'Telugu': 23,
        'Konkani': 24,
        'Bhojpuri': 25,
        'Kannada': 26,
        'Rajasthani': 27,
        'Malayalam': 28,
        'Hindi': 29,
        'Manipuri': 30,
        'Urdu': 31,
        'Nepali': 32,
        'Haryana': 33,
        'Punjab': 34,
        'Goa': 35,
        'Chhattisgarh': 36,
        'Kerala': 37,
        'Bihar': 38,
        'Tamil Nadu': 39,
        'Jharkhand': 40,
        'Meghalaya': 41,
        'Delhi': 42,
        'Assam': 43,
        'Madhya Pradesh': 44,
        'West Bengal': 45,
        'Rajasthan': 46,
        'Uttar Pradesh': 47,
        'Telangana': 48,
        'Andhra Pradesh': 49,
        'Himachal Pradesh': 50,
        'Nagaland': 51,
        'Gujarat': 52,
        'Arunachal Pradesh': 53,
        'Maharashtra': 54,
        'Odisha': 55,
        'Tripura': 56,
        'Uttarakhand': 57,
        'Karnataka': 58,
        'Jammu & Kashmir': 59
    }

def initilalize_features():

    global user_features

    for i in range(924):
        user = i+1
        user_vector = []
        for j in range(60):
            user_vector.append(0)
        user_features[user] = user_vector

def final_mapping_features_in_int():

    global user_features
    global user_features_1

    for i in range(924):
        user_features_1[i+1] = map(int, user_features[i+1])
    #print user_features_1
    with open("/home/diksha/IIITD/sem4/capstone/final files/final_files/users_features_dictionary", 'w') as myfile:
        myfile.write(json.dumps(user_features_1))
    myfile.close()
    print 'writing over'

def map_age():

    global user_features

    print 'mapping age'
    with open("map_user_age") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])
            age_index = int(line[1]) / 10
            user_features[user][age_index] = 1
            #print user_features[user]

def map_gender():

    global user_features
    global features

    print 'mapping gender'
    with open("map_user_gender") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])
            gender = line[1].rstrip()
            user_features[user][features[gender]] = 1
            #print user_features[user]


def map_job():

    global user_features
    global features

    print 'mapping job'
    with open("map_user_job") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])
            job = line[1].rstrip()
            user_features[user][features[job]] = 1
            #print user_features[user]


def map_language():

    global user_features
    global features

    print 'mapping language'
    with open("map_user_language") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])
            language = line[1].rstrip()
            user_features[user][features[language]] = 1
            #print user_features[user]

def map_state():

    global user_features
    global features

    print 'mapping state'
    with open("map_user_state") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])
            state = line[1].rstrip()
            user_features[user][features[state]] = 1
            #print user_features[user]



initilalize_features()
map_age()
map_gender()
map_job()
map_language()
map_state()
final_mapping_features_in_int()





