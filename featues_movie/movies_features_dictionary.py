import os
import json
import csv

movie_features = dict()
movie_features_1 = dict()
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

features = {
        'Swedish': 0,
        'Swahili': 1,
        'Telugu': 2,
        'Hebrew': 3,
        'Marathi': 4,
        'Oriya': 5,
        'Gujarati': 6,
        'Tulu': 7,
        'Hindi': 8,
        'Dutch': 9,
        'Mandarin': 10,
        'Sanskrit': 11,
        'Manipuri': 12,
        'Awadhi': 13,
        'Sinhalese': 14,
        'Shanghainese': 15,
        'Danish': 16,
        'Indonesian': 17,
        'Latin': 18,
        'Hungarian': 19,
        'Ukrainian': 20,
        'Berberlanguages': 21,
        'Turkish': 22,
        'Sindhi': 23,
        'Malay': 24,
        'French': 25,
        'Dari': 26,
        'Bengali': 27,
        'Romanian': 28,
        'Hokkien': 29,
        'Thai': 30,
        'Italian': 31,
        'Tamil': 32,
        'IndianSignLanguage': 33,
        'Ladakhi': 34,
        'Nepali': 35,
        'Filipino': 36,
        'Pushto': 37,
        'Cantonese': 38,
        'Armenian': 39,
        'Panjabi': 40,
        'Russian': 41,
        'Tagalog': 42,
        'English': 43,
        'Malayalam': 44,
        'Rajasthani': 45,
        'Konkani': 46,
        'Assamese': 47,
        'Portuguese': 48,
        'Chhattisgarhi': 49,
        'Haryanvi': 50,
        'Bhojpuri': 51,
        'Chinese': 52,
        'Greek': 53,
        'German': 54,
        'Tibetan': 55,
        'Kazakh': 56,
        'Japanese': 57,
        'Kannada': 58,
        'Persian': 59,
        'Spanish': 60,
        'Urdu': 61,
        'Arabic': 62,
        'Mystery': 63,
        'Romance': 64,
        'History': 65,
        'Sport': 66,
        'Sci-Fi': 67,
        'Family': 68,
        'Horror': 69,
        'Crime': 70,
        'Drama': 71,
        'Fantasy': 72,
        'War': 73,
        'Animation': 74,
        'Music': 75,
        'Biography': 76,
        'Action': 77,
        'News': 78,
        'Western': 79,
        'Comedy': 80,
        'Adventure': 81,
        'Thriller': 82,
        'Musical': 83
    }


def initilalize_features():

    global movie_features

    for i in range(2850):
        movie = i+1
        movie_vector = []
        for j in range(84):
            movie_vector.append(0)
        movie_features[movie] = movie_vector

def final_mapping_features_in_int():

    global movie_features
    global movie_features_1

    for i in range(2850):
        movie_features_1[i+1] = map(int, movie_features[i+1])
    print movie_features_1
    with open("/home/diksha/IIITD/sem4/capstone/final files/final_files/movie_features_dictionary", 'w') as myfile:
        myfile.write(json.dumps(movie_features_1))
    myfile.close()
    print 'writing over'


def map_language():

    global movie_features
    global features

    print 'mapping language'
    with open("map_movie_language") as myFile:
        for line in myFile:
            line = line.split("  ")
            movie = int(line[0])
            language = line[1].rstrip()
            movie_features[movie][features[language]] = 1
            #print movie_features[movie]


def map_genre():

    global movie_features
    global features

    print 'mapping genre'
    with open("map_movie_genre") as myFile:
        for line in myFile:
            line = line.split("  ")
            movie = int(line[0])
            genre = line[1].rstrip()
            movie_features[movie][features[genre]] = 1
            #print movie_features[movie]




initilalize_features()
map_language()
map_genre()
final_mapping_features_in_int()





