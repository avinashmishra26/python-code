#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:57:27 2021

@author: avinashkumarmishra
"""

import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


x = tf.constant([1,2,3])
y= tf.constant([4,5,6])

z = tf.add(x,y)
print(z)

z = x+y
print(z)

z = tf.subtract(x,y)
print(z)


z_ = tf.divide(x,y)
print(z_)


z_ = tf.multiply(x,y)
print(z_)

z__ = tf.tensordot(x, y, axes = 1)
z_n = x*y
print(z__, z_n)

z = x**3
print(z)


x_ = tf.random.normal((2,3))
y_ = tf.random.normal((3,2))

x_dot_y = tf.tensordot(x_,y_, axes = 1)
print(x_dot_y)

x_dot_y = tf.matmul(x_,y_)
print(x_dot_y)


x_dot_y = x_ @ y_
print(x_dot_y)