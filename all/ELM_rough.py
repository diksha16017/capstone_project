import numpy as np
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
    with open("train1") as my_file:
        for line in my_file:
            count = count + 1
            split_line = line.split("  ")
            user = split_line[0]
            movie = split_line[1]
            rating = int(split_line[2])
            X_train.append(user_features[user] + movie_features[movie])
            rating_index = rating + 1
            ratings = [0, 0, 0]
            ratings[rating_index] = 1
            Y_train.append(ratings)
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
    with open("test1") as my_file:
        for line in my_file:
            count = count + 1
            split_line = line.split("  ")
            user = split_line[0]
            movie = split_line[1]
            rating = int(split_line[2])
            X_test.append(user_features[user] + movie_features[movie])
            rating_index = rating + 1
            ratings = [0, 0, 0]
            ratings[rating_index] = 1
            Y_test.append(ratings)
            # if count == 3:
            #     print len(X_test[2])
            #     print X_test
            #     print Y_test

    return X_test, Y_test

def sigmoid_activation(mat):
    return 1 / (1 + np.exp(-mat))

def neural_network_train(X_train, Y_train):

    ip_layer_neuron_number = len(X_train[0])
    hidden_layer_neuron_number = 4 * ip_layer_neuron_number

    mean = np.mean(X_train)
    std_deviation = np.std(X_train)
    w1 = std_deviation * np.random.randn(ip_layer_neuron_number, hidden_layer_neuron_number) + mean
    hidden_activation = sigmoid_activation(np.dot(X_train, w1))
    w2 = np.linalg.lstsq(hidden_activation, Y_train)[0]
    return w1, w2

def find_predicted_ratings(X_test, w1, w2):

    hidden_activation = sigmoid_activation(np.dot(X_test, w1))
    output_activation = np.dot(hidden_activation, w2)
    predicted_ratings = []

    for line in output_activation:

        prediction_array = [0, 0, 0]
        max_rating_index = np.argmax(line)
        prediction_array[max_rating_index] = 1
        predicted_ratings.append(list(prediction_array))

    #print predicted_ratings
    return predicted_ratings

def find_Accuracy_MAE(predicted_ratings, Y_test):

    matched = 0
    MAE = 0.0

    for i in range(len(Y_test)):
        actual_rating = Y_test[i]
        predicted_rating = predicted_ratings[i]
        MAE = MAE + abs((actual_rating.index(1)-1) - (predicted_rating.index(1)-1))
        if actual_rating.index(1) == predicted_rating.index(1):
            matched += 1
    accuracy = float(matched) / len(Y_test)
    accuracy = accuracy * 100
    MAE = MAE / len(Y_test)
    print accuracy
    print MAE


X_train, Y_train = create_training_data()
print 'create tarining data over....'

X_test, Y_test = create_testing_data()
print 'create testing data over....'

w1, w2 = neural_network_train(X_train, Y_train)
print 'neural network training over....'

predicted_ratings = find_predicted_ratings(X_test, w1, w2)
print 'calculation of predicted ratings over....'

find_Accuracy_MAE(predicted_ratings, Y_test)