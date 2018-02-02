import numpy as np
import pandas as pd
import os
from sklearn import cross_validation as cv


os.chdir("/home/diksha/IIITD/sem4/capstone/final files/final_files")
print 'hello'

header = ['user_id', 'movie_id', 'rating']
df = pd.read_csv('final_ratings', sep='  ', names=header)
#print df
df = df.sample(frac=1).reset_index(drop=True)

train_data, test_data = cv.train_test_split(df, test_size=0.20)
np.savetxt('train5', train_data.values, fmt='%d', delimiter="  ")
np.savetxt('test5', test_data.values, fmt='%d', delimiter="  ")
print 'train data'
#print train_data
print len(train_data)
print 'test data'
#print test_data
print len(test_data)