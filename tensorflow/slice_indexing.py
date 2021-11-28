#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:09:28 2021

@author: avinashkumarmishra
"""

import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


x = tf.constant([[1,2,3,4],[5,6,7,8]])
print(x[0])

print(type(x))

print(x[:,0])


print(x[1,:])


print(x[0:2,:])

print(x[0,1:3])


y = tf.random.normal((2,3))
print(y)
print('here:::',type(x))

y = tf.random.normal((3,2))
print(y)

y = tf.reshape(y, (-1,2))
print(y)

y = tf.reshape(y, (6))
print(y)


#Convert to numpy and vice-versa
y = y.numpy()
print(y)
print(type(y))


y = tf.convert_to_tensor(y)
print(y)
print(type(y))

