#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 03:54:10 2021

@author: avinashkumarmishra
"""

import torch
import torch.nn as nn
import torchvision
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

transform = transforms.Compose([transforms.ToTensor(), \
                                transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))])

train_dataset = datasets.CIFAR10(root = 'data/cifar10', train = True, \
                                             transform = transforms.ToTensor(), \
                                             download = True)
    
    
test_dataset = datasets.CIFAR10(root = 'data/cifar10', train = False, \
                                             transform = transforms.ToTensor(), \
                                             download = True)
    
batch_size = 4
    
train_loader = DataLoader(dataset = train_dataset, batch_size=batch_size, shuffle = True)

test_loader = DataLoader(dataset = test_dataset, batch_size=batch_size, shuffle = True)


itr = train_loader.__iter__()
images,labels = itr.__next__()


def imshow(img):
    img = img/2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1,2,0)))
    plt.show()

for img in images:
    #imshow(torchvision.utils.make_grid(img))
    break

imshow(torchvision.utils.make_grid(images))

x = torch.empty(3, 32, 32)
imshow(torchvision.utils.make_grid(x))