#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:33:15 2021

@author: avinashkumarmishra
"""


import torch
import numpy as np

x = torch.tensor([1,2,3, 4], dtype=torch.float64)


x1 = x.numpy()

x.add_(1)

print('x1', x1, type(x1))


y = np.ones(5)

y1 = torch.from_numpy(y)


y1.add_(1)
print('y', y, 'y1', y1, type(y1))