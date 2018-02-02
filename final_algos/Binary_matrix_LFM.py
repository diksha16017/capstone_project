import numpy as np
from copy import deepcopy
import os

k = 20
count = 10
totalMovies = 2850
totalUsers = 924
Y = np.zeros((totalUsers, totalMovies))
R = np.zeros((totalUsers, totalMovies))

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

def readTrainData():

    print 'train1'
    global Y
    with open("train1") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            Y[user, movie] = rating
    XO = deepcopy(Y)
    return XO

def initialize(XO):

    global R
    for i in range(len(XO)):
        for j in range(len(XO[0])):
            if XO[i][j] == 0:
                row = np.mean(XO[i, :])
                column = np.mean(XO[:, j])
                mean_ = float((row + column)/2.0)
                XO[i][j] = mean_
            else:
                R[i][j] = 1

    return XO

def latent_method(XO):

    global R
    global Y
    global count
    while count > 0:
        print count
        count = count - 1
        B = XO + (Y - np.multiply(R, XO))
        UK, VK = matrix_factorisation(B)
        XO = np.dot(UK, VK)

    ratings = np.dot(UK, VK)
    return ratings

def matrix_factorisation(B):

    count1 = 20
    global k
    global totalUsers
    lamb_reg = [0.01] * k
    U = np.random.randint(low=1, high=2, size=(totalUsers, k))
    while count1 > 0:
        count1 = count1 - 1
        U_trans = np.transpose(U)
        VK = np.linalg.lstsq(np.dot(U_trans, U) + np.diag(lamb_reg), np.dot(np.transpose(U), B))[0]
        VK_trans = np.transpose(VK)
        R_trans = np.transpose(B)
        UK_temp = np.linalg.lstsq(np.dot(VK, VK_trans) + np.diag(lamb_reg), np.dot(VK, R_trans))[0]
        UK = np.transpose(UK_temp)
        U = UK
        if np.array_equal(np.dot(UK, VK), B) == True:
            break
    return UK, VK


def testing(ratings):

    records = 0
    total_mae = 0.0
    print 'testing method'
    os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
    with open("test1") as myFile:
        for line in myFile:
            records = records + 1
            line = line.split("  ")
            user = int(line[0]) - 1
            movie = int(line[1])
            movie = movie - 1
            actual_rating = int(line[2])
            predicted_rating = ratings[user][movie]
            print actual_rating, round(predicted_rating)
            total_mae = total_mae + abs(predicted_rating - actual_rating)
    print 'mae'
    mae = total_mae/records
    print mae
    print 'nmae'
    print mae/4.0



XO = readTrainData()
print 'reading over'
XO = initialize(XO)
print 'initialize over'
ratings = latent_method(XO)
print 'lfm over'
testing(ratings)
