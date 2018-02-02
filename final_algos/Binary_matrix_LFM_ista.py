import numpy as np
from copy import deepcopy
import os
from numpy import linalg as LA


totalMovies = 2850
totalUsers = 924
Y = np.zeros((totalUsers, totalMovies))
R = np.zeros((totalUsers, totalMovies))

count = 10
k = 10

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

#function for reading training data
def readTrainData():

    global Y
    print 'train5'
    with open("train5") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            Y[user, movie] = rating

    XO = deepcopy(Y)
    return XO

#funtion for initializing matrices
def initialize(XO):


    global R
    global Y
    for i in range(len(XO)):
        for j in range(len(XO[i])):
            if XO[i][j] == 0:
                row = np.mean(Y[i, :])
                #print row
                column = np.mean(Y[:, j])
                #print column
                mean_ = (row + column)/2.0
                XO[i][j] = mean_
            else:
                R[i][j] = 1

    return XO

# main loop for calculating B and from here calling alternating minimization function
def latent_method(XO):

    global count
    global R
    global Y
    while count > 0:
        print count
        count = count - 1
        B = XO + (Y - np.multiply(R, XO))
        UK, VK = matrix_factorisation(B)
        XO = np.dot(UK, VK)
    return UK, VK

# l1 norm algorithm
def ista(B, lamb, U):
    global k
    global totalMovies
    VO = np.zeros((totalMovies, k))
    VK = np.zeros((totalMovies, k))
    w, v = LA.eig(np.dot(U, np.transpose(U)))
    alpha = np.amax(w)
    for loop in range(11):
        T = VO + np.transpose((1/alpha)*(np.dot(np.transpose(U), (B - np.dot(U, np.transpose(VO))))))
        signMatrix = np.sign(T)
        for i in range(len(T)):
            for j in range(len(T[0])):
                val = abs(T[i][j]) - (lamb/(2 * alpha))
                if val < 0.0:
                    val = 0.0
                VK[i][j] = signMatrix[i][j] * val
        VO = VK
    lamda_matrix = np.zeros((k, k))
    np.fill_diagonal(lamda_matrix, lamb)
    VK = np.dot(VK, lamda_matrix)
    return VK

#alternating minimization problem algorithm
def matrix_factorisation(B):
    count1 = 10
    global k
    global totalUsers
    global totalMovies
    lamb_reg = [0.01] * k
    lamb = 0.01
    U = np.random.randint(low=1, high=2, size=(totalUsers, k))
    while count1 > 0:
        count1 = count1 - 1
        U_trans = np.transpose(U)
        VK = np.linalg.lstsq(np.dot(U_trans, U), np.dot(np.transpose(U), B))[0] + np.transpose(ista(B, lamb, U))
        #VK[VK < 0] = 0
        VK_trans = np.transpose(VK)
        R_trans = np.transpose(B)
        UK_temp = np.linalg.lstsq(np.dot(VK, VK_trans) + np.diag(lamb_reg), np.dot(VK, R_trans))[0]
        UK = np.transpose(UK_temp)
        #UK[UK < 0] = 0
        U = UK
        if np.array_equal(np.dot(UK, VK), B) == True:
            break
    return UK, VK

def testing (UK, VK):

    records = 0
    total_mae = 0.0
    print 'testing method'
    ratings = np.dot(UK, VK)
    os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
    with open("test5") as myFile:
        for line in myFile:
            records = records + 1
            line = line.split("  ")
            user = int(line[0]) - 1
            movie = int(line[1])
            movie = movie - 1
            actual_rating = int(line[2])
            predicted_rating = ratings[user][movie]
            total_mae = total_mae + abs(predicted_rating - actual_rating)
    print 'mae'
    mae = total_mae/records
    print mae
    print 'nmae'
    print mae/4.0

XO = readTrainData()
print 'done reading training data'
XO = initialize(XO)
print 'done initializing'
UK, VK = latent_method(XO)
print 'latent method over'
testing(UK, VK)