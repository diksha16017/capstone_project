# item auto-encoder

import tensorflow as tf
import numpy as np


training_dataset = "/home/diksha/IIITD/sem4/capstone/final files/final_files/train1"
test_dataset = "/home/diksha/IIITD/sem4/capstone/final files/final_files/test1"

learning_rate = 0.01
num_steps = 4000
lamb = 0.01
display_step = 100
batch_size = 2850

num_hidden_nodes = 100
num_input = 924

X = tf.placeholder("float", [None, num_input])
R = tf.placeholder("float", [None, num_input])

weights = {
    'encoder': tf.Variable(tf.random_normal([num_input, num_hidden_nodes])),
    'decoder': tf.Variable(tf.random_normal([num_hidden_nodes, num_input])),
}

biases = {
    'encoder': tf.Variable(tf.random_normal([num_hidden_nodes])),
    'decoder': tf.Variable(tf.random_normal([num_input])),
}


# In[3]:


def encoder(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder']), biases['encoder']))
    return layer_1


def decoder(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder']), biases['decoder']))
    return layer_1


encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

y_pred = decoder_op
y_true = X

loss = tf.reduce_mean(
    tf.pow(y_true - y_pred * R, 2) + (lamb / 2) * (tf.norm(weights['encoder']) + tf.norm(weights['decoder'])))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

totalMovies = 2850
totalUsers = 924

user_item_matrix = np.zeros((totalMovies, totalUsers))
binary_matrix = np.zeros((totalMovies, totalUsers))

with open(training_dataset) as myFile:
    for line in myFile:
        line = line.split("  ")
        user = int(line[0]) - 1
        movie = int(line[1]) - 1
        rating = int(line[2])
        user_item_matrix[movie, user] = rating
        if rating != 0:
            binary_matrix[movie, user] = 1

scaled_user_item_matrix = np.divide(user_item_matrix - np.min(user_item_matrix), 1)

for i in range(1, num_steps + 1):

    _, l = sess.run([optimizer, loss], feed_dict={X: scaled_user_item_matrix, R: binary_matrix})

    if i % display_step == 0 or i == 1:
        print('Step %i: Batch Loss: %f' % (i, l))

predicted_ratings = sess.run(decoder_op, feed_dict={X: scaled_user_item_matrix, R: binary_matrix})
print(np.shape(predicted_ratings))

MAE = 0
number_of_records = 0

with open(test_dataset) as my_file:
    for line in my_file:
        line = line.split("  ")
        user = int(line[0]) - 1
        movie = int(line[1]) - 1
        actual_rating = int(line[2])
        number_of_records += 1
        actual_predicted_rating = predicted_ratings[movie][user] * 1
        if actual_predicted_rating > 1:
            actual_predicted_rating = 1
        if actual_predicted_rating < -1:
            actual_predicted_rating = -1
        print actual_rating, round(actual_predicted_rating)
        MAE += (abs(round(actual_predicted_rating) - actual_rating))

MAE = MAE / (number_of_records)

print ('Final mae error is : ')
print (str(MAE))


