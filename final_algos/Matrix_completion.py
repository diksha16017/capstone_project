import numpy as np
import os

totalMovies = 2850
totalUsers = 924

lamb = 0.01
Y = np.zeros((totalUsers, totalMovies))
R = np.zeros((totalUsers, totalMovies))

count = 20

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

def readTrainData():

    global Y
    print 'train1'
    with open("train1") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            Y[user, movie] = rating

def initialize():

    global R
    global Y
    for i in range(len(Y)):
        for j in range(len(Y[i])):
            if Y[i][j] != 0:
                R[i][j] = 1


def matrixCompletion():

    global count
    global lamb
    global R
    global Y
    XO = np.random.randint(low=1, high=2, size=(totalUsers, totalMovies))
    while count > 0:
        print count
        count = count - 1
        B = XO + (Y - np.multiply(R, XO))
        U, s, V = np.linalg.svd(B, full_matrices=True)
        #U[U < 0] = 0
        #V[V < 0] = 0
        sign_matrix = np.sign(s)
        for i in range(len(s)):
            val = abs(s[i]) - (lamb / 2)
            if val < 0.0:
                val = 0.0
            s[i] = sign_matrix[i] * val
        d = len(s)
        S = np.zeros((len(U), d))
        S = np.diag(s)
        temp1 = np.dot(U[:, 1:d], S[1:d, 1:d])
        XO = np.dot(temp1, np.transpose(V[:, 1:d]))
        #XO[XO < 0] = 0
    #XO[XO < 0] = 0
    #print 'final X predicted matrix'
    #print XO
    return XO

def testing(XO):

    records = 0
    total_mae = 0.0
    print 'testing method'
    os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
    with open("test1") as myFile:
        for line in myFile:
            records = records + 1
            line = line.split("  ")
            user = int(line[0]) - 1
            movie = int(line[1]) - 1
            actual_rating = int(line[2])
            predicted_rating = XO[user][movie]
            if predicted_rating > 1.0:
                predicted_rating = 1.0
            if predicted_rating < -1.0:
                predicted_rating = -1.0
            print actual_rating, round(predicted_rating)
            total_mae = total_mae + abs(round(predicted_rating) - actual_rating)
    print 'mae'
    mae = total_mae/records
    print mae

XO = readTrainData()
print 'done reading training data'
initialize()
print 'done initializing'
XO = matrixCompletion()
print 'matrix completion over'
#print np.shape(XO)
testing(XO)