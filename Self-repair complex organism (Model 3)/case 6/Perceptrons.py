# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:22:23 2020
@author: tnmthai
"""

import numpy as np

no_of_inputs=2
threshold=100
learning_rate=0.01

weights2=[-0.01,  0.01,  0.01]
weights3=[-0.2,  0.1,  0.1 , 0.1]
weights4=[-0.05, 0.01,  0.01,  0.03,  0.01]

def normalize(inputs):
    for i in range (len(inputs)):
        if inputs[i] !=0:
            inputs[i] = 1
    return inputs

def predict(inputs,weights):
    summation = np.dot(inputs, weights[1:]) + weights[0]
    if summation > 0:
        activation = 1
    else:
        activation = 0            
    return activation
   
def perceptron(inputs):

    inputs=normalize(inputs)

    if len(inputs)==2:
        return predict(inputs,weights2)
    elif len(inputs)==3:
        return predict(inputs,weights3)
    elif len(inputs)==4:
        return predict(inputs,weights4)
    else: 
        return -1


