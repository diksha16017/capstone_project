import numpy as np
import os

k = 20
count = 20
totalMovies = 2850
totalUsers = 924

R = np.zeros((totalUsers, totalMovies))
U = np.random.rand(totalUsers, k)
os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")

def readTrainData():

    global R
    with open("train1") as myFile:
        for line in myFile:
            line = line.split("  ")
            user = int(line[0])-1
            movie = int(line[1])
            movie = movie-1
            rating = int(line[2])
            R[user, movie] = rating

def matrix_factorisation():

    global count
    global R
    global U
    while count > 0:
        print count
        count = count - 1
        VK = np.linalg.lstsq(U, R)[0]
        VK[VK < 0] = 0
        UK_temp = np.linalg.lstsq(np.transpose(VK), np.transpose(R))[0]
        UK = np.transpose(UK_temp)
        UK[UK < 0] = 0
        U = UK
        if np.array_equal(np.dot(UK, VK), R) == True:
            break

    R_final = np.dot(UK, VK)
    R_final[R_final < 0] = 0
    return R_final

def testing (ratings):

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

readTrainData()
ratings = matrix_factorisation()
testing(ratings)