import numpy as np
import os

k = 20
count = 30
totalMovies = 2850
totalUsers = 924

R = np.zeros((totalUsers, totalMovies))
U = np.random.randint(low=1, high=2, size=(totalUsers, k))

os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

def readTrainData():

    global R
    with open("train5") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            R[user, movie] = rating



def matrix_factorisation():

    global R
    global U
    global k
    global count

    lamb_reg = [0.01] * k
    while count > 0:
        print count
        count = count - 1
        U_trans = np.transpose(U)
        VK = np.linalg.lstsq(np.dot(U_trans, U) + np.diag(lamb_reg), np.dot(np.transpose(U), R))[0]
        VK[VK < 0] = 0
        VK_trans = np.transpose(VK)
        R_trans = np.transpose(R)
        UK_temp = np.linalg.lstsq(np.dot(VK, VK_trans) + np.diag(lamb_reg), np.dot(VK, R_trans))[0]
        UK = np.transpose(UK_temp)
        UK[UK < 0] = 0
        U = UK
        if np.array_equal(np.dot(UK, VK), R) == True:
            break

    R_final = np.dot(UK, VK)
    R_final[R_final < 0] = 0
    return R_final


def testing(ratings):

    records = 0
    total_mae = 0.0
    print 'testing method'
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
            print actual_rating, round(predicted_rating)
            total_mae = total_mae + abs(predicted_rating - actual_rating)
    print 'mae'
    mae = total_mae/records
    print mae
    print 'nmae'
    print mae/4.0


readTrainData()
ratings = matrix_factorisation()
testing(ratings)