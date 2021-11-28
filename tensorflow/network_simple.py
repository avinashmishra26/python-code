#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: avinashkumarmishra
"""

import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


mnist = keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

print(x_train.shape,x_test.shape)

#normalize
x_train, x_test = x_train/255.0, x_test/255.0

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(x_train[i], cmap='gray')
plt.show()

# model creation

model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10)
        ])

print(model.summary())

#different way
# model = keras.Sequential()
# model.add(keras.layers.Flatten(input_shape=(28,28)))
# model.add(keras.layers.Dense(128, activation='relu'))
# model.add(keras.layers.Dense(10))
# print(model.summary())

#model.compile()

#loss and optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True)
optim = keras.optimizers.Adam(lr = 0.001)
metrics = ["accuracy"]

model.compile(loss = loss, optimizer=optim, metrics=metrics)

#training
batch_size = 64
epochs = 5

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, shuffle=True, verbose=2)

#evaluate
model.evaluate(x_test, y_test,batch_size=batch_size, verbose = 2 )


print('One way of prediction' , end='*********\n')
#predictions
probability_model = keras.models.Sequential([
    model,
    keras.layers.Softmax()
    ])

predictions = probability_model(x_test)
pred0 = predictions[0]
print(pred0)
labels0 = np.argmax(pred0)
print(labels0)

print('Another way of prediction' , end='*********\n')
#another way
predictions = model(x_test)
predictions = tf.nn.softmax(predictions)
print(pred0)
labels0 = np.argmax(pred0)
print(labels0)

print('3rd way of prediction' , end='*********\n')
predictions = model.predict(x_test, batch_size=batch_size)
predictions = tf.nn.softmax(predictions)
pred0_5 = predictions[0:5]
print(pred0_5.shape)
label0_5 = np.argmax(pred0_5, axis=1)
print(label0_5)



