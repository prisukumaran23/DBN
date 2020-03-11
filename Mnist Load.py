#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:28:12 2019
Loading Mnist data
@author: priyankasukumaran
"""

import numpy as np
import matplotlib.pyplot as plt

data_path = "/Users/priyankasukumaran/Documents/PhD Neural Dynamics/Year 1/Comp Mini Project/"
'''
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

test_binary = np.zeros((10000,784))

for j in range (0,10000):
    for i in range (1,784):
        if test_data[j,i] >= 178:
            test_binary[j,i-1] = 1
        else:
            test_binary[j,i-1] = 0
np.savetxt('test_binary.csv', test_binary, delimiter=',')

train_binary = np.zeros((60000,784))

for j in range (0,60000):
    for i in range (1,784):
        if train_data[j,i] >= 178:
            train_binary[j,i-1] = 1
        else:
            train_binary[j,i-1] = 0
np.savetxt('train_binary.csv', train_binary, delimiter=',')
        

im1 = train_binary[50,:].reshape(28,28)
print(im1.shape)      
print(im1)
plt.imshow(im1, cmap="Greys")
'''

train_data = np.loadtxt(data_path + "train_binary.csv", delimiter=",")
test_data = np.loadtxt(data_path + "test_binary.csv", delimiter=",")
