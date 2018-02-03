import numpy as np
from sklearn.linear_model import OrthogonalMatchingPursuit
import os
import json

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

with open("users_features_dictionary") as userfile:
    user_features = json.load(userfile)


with open("movie_features_dictionary") as moviefile:
    movie_features = json.load(moviefile)

def create_training_data():


    global movie_features
    global user_features
    X_train = []
    Y_train = []
    count = 0
    with open("train5") as my_file:
        for line in my_file:
            count = count + 1
            split_line = line.split("  ")
            user = split_line[0]
            movie = split_line[1]
            rating = int(split_line[2])
            X_train.append(user_features[user] + movie_features[movie])
            Y_train.append(rating)
            # if count == 3:
            #     print len(X_train[2])
            #     print X_train
            #     print Y_train

    return X_train, Y_train

def create_testing_data():


    global movie_features
    global user_features
    X_test = []
    Y_test = []
    count = 0
    with open("test5") as my_file:
        for line in my_file:
            count = count + 1
            split_line = line.split("  ")
            user = split_line[0]
            movie = split_line[1]
            rating = int(split_line[2])
            X_test.append(user_features[user] + movie_features[movie])
            Y_test.append(rating)
            # if count == 3:
            #     print len(X_test[2])
            #     print X_test
            #     print Y_test

    return X_test, Y_test

def mySRC(X_train_array, Y_train_array, X_test_array):
    print 'SRC'
    src1 = OrthogonalMatchingPursuit()
    src1.fit(X_train_array, Y_train_array)
    predict = src1.predict(X_test_array)
    return predict

def prediction_function(predict, Y_test_array):

    MAE = 0.0
    matched = 0
    print 'predict'
    for i in range(len(Y_test_array)):
        predicted_rating_round = round(predict[i])
        actual_rating = Y_test_array[i]
        MAE = MAE + abs(actual_rating - predicted_rating_round)
        if actual_rating == predicted_rating_round:
            matched = matched + 1

    accuracy = float(matched) / len(Y_test_array)
    MAE = MAE / len(Y_test_array)
    print 'Accuracy : ', accuracy*100
    print 'MAE : ', MAE


X_train, Y_train = create_training_data()
X_train_array = np.array(X_train)
Y_train_array = np.array(Y_train)
print 'create tarining data over....'
X_test, Y_test = create_testing_data()
X_test_array = np.array(X_test)
Y_test_array = np.array(Y_test)
predict = mySRC(X_train_array, Y_train_array, X_test_array)
prediction_function(predict, Y_test_array)