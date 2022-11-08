# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:22:26 2022

@author: Jordan Turley
"""

#%% Imports
import pandas as pd

#%% Read in data
data = pd.read_csv(r'C:\Users\Jordan Turley\Documents\GitHub\AdventOfCode2020\Inputs\3.txt', header = None)
#data = pd.read_csv(r'C:\Users\Jordan Turley\Documents\GitHub\AdventOfCode2020\Inputs\3sample.txt', header = None)
data.columns = ['input']

#%% Part 1
data = data['input'].str.split('',expand = True)
data = data.iloc[:,:-1].iloc[:,1:]

positionx = 0
positiony = 0

#step size
stepx = 3
stepy = 1

value_output = []

while(1):
    print('1')
    #new location
    positionx = positionx + stepx
    positiony = positiony + stepy


    if positionx>data.shape[1]-1:
        positionx = positionx-data.shape[1]
    if positiony>data.shape[0]-1:
        finish = True
        break
    #get value
    value = data.iloc[positiony,positionx]
    value_output = value_output + [value]
    
from collections import Counter
print(Counter(value_output)['#'])

#%% Part 2


output = 1
step_sizes = ['11','31','51','71','12']
for step_size in step_sizes:
    positionx = 0
    positiony = 0
    #step size
    stepx = int(step_size[0])
    stepy = int(step_size[1])
    
    value_output = []
    
    while(1):
        print('1')
        #new location
        positionx = positionx + stepx
        positiony = positiony + stepy
    
    
        if positionx>data.shape[1]-1:
            positionx = positionx-data.shape[1]
        if positiony>data.shape[0]-1:
            finish = True
            break
        #get value
        value = data.iloc[positiony,positionx]
        value_output = value_output + [value]
        
    from collections import Counter
    count = Counter(value_output)['#']
    output = output*count