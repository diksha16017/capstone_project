import numpy as np
import os


totalMovies = 2850
totalUsers = 924

Y = np.zeros((totalUsers, totalMovies))
R = np.zeros((totalUsers, totalMovies))

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

def readTrainData():

    global Y

    print '3'
    with open("train3") as myFile:

        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            Y[user,movie] = rating

#funtion for initializing matrices
def initialize():

    global Y
    global R
    for i in range(len(Y)):
        for j in range(len(Y[i])):
            if Y[i][j] != 0:
                R[i][j] = 1



def N_norm():

    global Y
    global R
    global totalMovies
    global totalUsers
    lamb = 80
    print lamb
    count = 11
    #print count
    X = np.random.randint(low=1, high=2, size=(totalUsers, totalMovies))

    for i in range(count):
        print i
        B = X + (Y - R * X)
        U, S, V = np.linalg.svd(B, full_matrices=False)
        S = np.maximum(S - (lamb/2),0)
        X = np.linalg.multi_dot([U, np.diag(S), V])

    return X

def testing (X):

    records = 0
    total_mae = 0.0
    print 'testing method'
    ratings = X
    os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
    with open("test3") as myFile:
        for line in myFile:
            records = records + 1
            line = line.split("  ")
            user = int(line[0]) - 1
            movie = int(line[1])
            movie = movie - 1
            actual_rating = int(line[2])
            predicted_rating = ratings[user][movie]
            #predicted_rating = round(predicted_rating)
            print actual_rating, predicted_rating
            total_mae = total_mae + abs(predicted_rating - actual_rating)
    print 'mae'
    mae = total_mae/records
    print mae

readTrainData()
initialize()
X = N_norm()
testing(X)