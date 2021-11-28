#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 22:13:53 2021

@author: avinashkumarmishra
"""

import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


x = tf.constant([1,2,4])
print(x)


x = tf.Variable([1,2,3])
print(x)

x = tf.constant(['Avinash', 'Athesh'])
print(x)